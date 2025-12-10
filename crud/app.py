# app.py
import streamlit as st
from database import add_product, get_all_products, update_product, delete_product
 
# ---------------- CSS STYLING ----------------
def local_css():
    st.markdown("""
        <style>
            .stApp { 
                background-color: #f8f9fa;
                color: #222;
                font-family: 'Segoe UI', sans-serif;
            }
            .title {
                font-size: 32px;
                font-weight: bold;
                color: #007BFF;
                margin-bottom: 5px;
            }
            .subtitle {
                font-size: 14px;
                color: #666;
                margin-bottom: 20px;
            }
            .card {
                background: #fff;
                # padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .stButton>button {
                background-color: #007BFF;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                border: none;
            }
            .stButton>button:hover {
                background-color: #0056b3;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #007BFF;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)
 
local_css()
 
# ---------------- UI SECTION ----------------
st.markdown("<div class='title'>📦 Inventory Management System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Add, view, update, or delete products easily.</div>", unsafe_allow_html=True)
 
menu = ["Add Product", "View Inventory", "Update Product", "Delete Product"]
choice = st.sidebar.selectbox("Menu", menu)
 
# ---------------- ADD PRODUCT ----------------
if choice == "Add Product":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Add New Product")
 
    name = st.text_input("Product Name")
    qty = st.number_input("Quantity", min_value=0, step=1)
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    supplier = st.text_input("Supplier")
 
    if st.button("Add Product"):
        if name.strip() == "":
            st.error("Please enter a product name.")
        else:
            add_product(name, qty, price, supplier)
            st.success(f"✅ {name} added successfully!")
    st.markdown("</div>", unsafe_allow_html=True)
 
# ---------------- VIEW INVENTORY ----------------
elif choice == "View Inventory":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("All Inventory Items")
 
    data = get_all_products()
    if len(data) == 0:
        st.info("No products available.")
    else:
        table_html = "<table><tr><th>ID</th><th>Name</th><th>Quantity</th><th>Price</th><th>Supplier</th></tr>"
        for row in data:
            table_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
        table_html += "</table>"
        st.markdown(table_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
 
# ---------------- UPDATE PRODUCT ----------------
elif choice == "Update Product":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Update Stock / Price")
 
    data = get_all_products()
    ids = [str(row[0]) for row in data]
    if not ids:
        st.warning("No products available.")
    else:
        selected_id = st.selectbox("Select Product ID", ids)
        selected_data = None
        for row in data:
            if str(row[0]) == selected_id:
                selected_data = row
                break
 
        if selected_data:
            name = st.text_input("Product Name", value=selected_data[1])
            qty = st.number_input("Quantity", min_value=0, value=selected_data[2], step=1)
            price = st.number_input("Price", min_value=0.0, value=float(selected_data[3]), format="%.2f")
            supplier = st.text_input("Supplier", value=selected_data[4])
 
            if st.button("Update Product"):
                update_product(selected_id, name, qty, price, supplier)
                st.success(f"✅ Product ID {selected_id} updated successfully!")
    st.markdown("</div>", unsafe_allow_html=True)
 
# ---------------- DELETE PRODUCT ----------------
elif choice == "Delete Product":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Delete Product")
 
    data = get_all_products()
    ids = [str(row[0]) for row in data]
    if not ids:
        st.warning("No products to delete.")
    else:
        pid = st.selectbox("Select Product ID", ids)
        if st.button("Delete Product"):
            delete_product(pid)
            st.success(f"🗑️ Product ID {pid} deleted successfully!")
    st.markdown("</div>", unsafe_allow_html=True)
 







