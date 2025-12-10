# database.py
import pymysql

# This imports the pymysql library, which is a Python package 
# used to connect and interact with MySQL databases.
 
# ---------- DATABASE CONNECTION ----------
def get_connection():
    """Establish connection with MySQL"""
    return pymysql.connect(
        host="localhost",
        user="root",       # MySQL username
        password="root",   # MySQL password
        database="inventorydb"
    )

# Defines a function get_connection that creates and returns a connection object to the MySQL database.
# The connect method takes parameters to specify the database server location (host), username (user), password (password), and the specific database to connect (database).
# This function centralizes connection details so they can be reused.

 
# ---------- CRUD FUNCTIONS ----------
def add_product(name, quantity, price, supplier):
    conn = get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO products (name, quantity, price, supplier) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (name, quantity, price, supplier))
    conn.commit()
    conn.close()

# Opens a connection and a cursor to interact with the database.
# Defines an SQL insert statement with placeholders (%s) for data values.
# Executes the SQL command with the actual product details (name, quantity, price, supplier) passed as parameters.
# Commits the transaction to save changes.
# Closes the connection.
 
def get_all_products():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    conn.close()
    return data

# Connects to the database and creates a cursor.
# Executes a simple SQL query to select all columns from the products table.
# Fetches all records returned by the query using fetchall().
# Closes the connection.
# Returns the fetched records.
 
def update_product(pid, name, quantity, price, supplier):
    conn = get_connection()
    cur = conn.cursor()
    sql = "UPDATE products SET name=%s, quantity=%s, price=%s, supplier=%s WHERE id=%s"
    cur.execute(sql, (name, quantity, price, supplier, pid))
    conn.commit()
    conn.close()
 
# Connects and creates a cursor.
# Defines an SQL update statement to modify product details identified by id (pid).
# Executes the update with new values for name, quantity, price, and supplier.
# Commits the changes and closes the connection.

def delete_product(pid):
    conn = get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM products WHERE id=%s"
    cur.execute(sql, (pid,))
    conn.commit()
    conn.close()

# Establishes connection and cursor.
# Uses an SQL delete command to remove a product by its id.
# Executes the delete query with the given product ID.
# Commits the transaction and closes connection.



# Summary
# The code provides utility functions to interact with a MySQL database named "inventorydb" via pymysql.
# Each CRUD operation (insert, select, update, delete) is implemented as a function.
# The connection details are encapsulated in get_connection() for reuse and modularity.
# Proper connection opening, committing changes, and closing is handled in each function to maintain database integrity.
# This structure is common in simple Python programs working with relational databases, helping organize the code and keeping database logic separated.
