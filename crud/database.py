# database.py
import pymysql
 
# ---------- DATABASE CONNECTION ----------
def get_connection():
    """Establish connection with MySQL"""
    return pymysql.connect(
        host="localhost",
        user="root",       # MySQL username
        password="root",   # MySQL password
        database="inventorydb"
    )
 
# ---------- CRUD FUNCTIONS ----------
def add_product(name, quantity, price, supplier):
    conn = get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO products (name, quantity, price, supplier) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (name, quantity, price, supplier))
    conn.commit()
    conn.close()
 
def get_all_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    conn.close()
    return data
 
def update_product(pid, name, quantity, price, supplier):
    conn = get_connection()
    cur = conn.cursor()
    sql = "UPDATE products SET name=%s, quantity=%s, price=%s, supplier=%s WHERE id=%s"
    cur.execute(sql, (name, quantity, price, supplier, pid))
    conn.commit()
    conn.close()
 
def delete_product(pid):
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM products WHERE id=%s"
    cur.execute(sql, (pid,))
    conn.commit()
    conn.close()
