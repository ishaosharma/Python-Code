import pymysql
import streamlit as st
 
def get_connection():
    """Create and return a MySQL connection using PyMySQL."""
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",        # your MySQL username
            password="root",    # your MySQL password
            database="ewaydb",
            cursorclass=pymysql.cursors.Cursor,
            autocommit=False
        )
        return conn
    except pymysql.MySQLError as err:
        st.error(f"Database connection error: {err}")
        return None
 
 
def create_bill(bill):
    """Insert a new bill into the database."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO eway_bills
            (bill_no, bill_from, bill_to, product_name, city_from, city_to, quantity, total_amount, gst_percent, vehicle_no)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, bill)
        conn.commit()
        return True
    except pymysql.MySQLError as err:
        st.error(f"Error inserting data: {err}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()
 
 
def get_all_bills():
    """Fetch all bills from the database."""
    conn = get_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM eway_bills ORDER BY id DESC")
        data = cursor.fetchall()
        return data if data else []
    except pymysql.MySQLError as err:
        st.error(f"Error fetching data: {err}")
        return []
    finally:
        cursor.close()
        conn.close()
 
 
def get_bill_by_id(bill_id):
    """Fetch a single bill by ID."""
    conn = get_connection()
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM eway_bills WHERE id=%s", (bill_id,))
        data = cursor.fetchone()
        return data
    except pymysql.MySQLError as err:
        st.error(f"Error fetching record: {err}")
        return None
    finally:
        cursor.close()
        conn.close()
 
 
def update_bill(bill_id, bill):
    """Update an existing bill in the database."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        sql = """
            UPDATE eway_bills SET
            bill_no=%s, bill_from=%s, bill_to=%s, product_name=%s,
            city_from=%s, city_to=%s, quantity=%s, total_amount=%s,
            gst_percent=%s, vehicle_no=%s
            WHERE id=%s
        """
        cursor.execute(sql, (*bill, bill_id))
        conn.commit()
        return True
    except pymysql.MySQLError as err:
        st.error(f"Error updating record: {err}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()
 
 
def delete_bill(bill_id):
    """Delete a bill from the database."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM eway_bills WHERE id=%s", (bill_id,))
        conn.commit()
        return True
    except pymysql.MySQLError as err:
        st.error(f"Error deleting record: {err}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()