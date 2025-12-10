import streamlit as st
import database as db

st.set_page_config(page_title="E-Way Bill Management", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #ffffff;
            padding: 1rem 2rem;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display: none;}

        div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
            background-color: #17a2b8 !important;
            color: white !important;
        }

        .stForm {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 2rem;
        }

        /* Action buttons: prevent wrapping */
        div[data-testid="column"]:last-child > div {
            display: flex !important;
            gap: 3px !important;
            flex-wrap: nowrap !important;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: center !important;
        }

        /* Style action buttons */
        button[key^="read_"],
        button[key^="edit_"],
        button[key^="delete_"] {
            padding: 5px 10px !important;
            font-size: 0.7rem !important;
            border-radius: 3px !important;
            font-weight: 500 !important;
            border: none !important;
            min-width: 50px !important;
            width: auto !important;
            height: 26px !important;
            margin: 0 !important;
            white-space: nowrap !important;
            line-height: 1 !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
        }

        /* Read button - Cyan */
        button[key^="read_"] {
            background-color: #17a2b8 !important;
            color: white !important;
        }
        button[key^="read_"]:hover {
            background-color: #138496 !important;
        }
        /* Edit button - Blue */
        button[key^="edit_"] {
            background-color: #007bff !important;
            color: white !important;
        }
        button[key^="edit_"]:hover {
            background-color: #0056b3 !important;
        }
        /* Delete button - Red */
        button[key^="delete_"] {
            background-color: #dc3545 !important;
            color: white !important;
        }
        button[key^="delete_"]:hover {
            background-color: #c82333 !important;
        }

        button[key^="read_"] p,
        button[key^="edit_"] p,
        button[key^="delete_"] p {
            color: white !important;
            margin: 0 !important;
            padding: 0 !important;
            font-size: 0.7rem !important;
            white-space: nowrap !important;
            line-height: 1 !important;
        }
        div[data-testid="column"]:last-child {
            overflow: visible !important;
            min-width: 170px !important;
        }
        div[data-testid="column"]:last-child > div {
            display: flex !important;
            gap: 3px !important;
            flex-wrap: nowrap !important;
            flex-direction: row !important;
        }
        div[data-testid="column"]:last-child [data-testid="column"] {
            min-width: fit-content !important;
            width: auto !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "action" not in st.session_state:
    st.session_state.action = None
if "edit_id" not in st.session_state:
    st.session_state.edit_id = None
if "show_details" not in st.session_state:
    st.session_state.show_details = None
if "delete_id" not in st.session_state:
    st.session_state.delete_id = None

# Header section
col_header1, col_header2 = st.columns([5, 1])
with col_header1:
    st.title("E-Way Bills Management System")
with col_header2:
    st.write("")  # Spacing
    if st.button("Add +", key="add_btn", use_container_width=True):
        st.session_state.action = "add"
        st.session_state.edit_id = None
        st.session_state.show_details = None
        st.rerun()

# Add/Edit Form
if st.session_state.action in ["add", "edit"]:
    if st.session_state.action == "edit":
        st.subheader("✏️ Edit E-Way Bill")
    else:
        st.subheader("➕ Add E-Way Bill")

    if st.session_state.edit_id:
        bill = db.get_bill_by_id(st.session_state.edit_id)
        if not bill:
            st.error("Bill not found!")
            st.session_state.action = None
            st.session_state.edit_id = None
            st.rerun()
    else:
        bill = None

    with st.form("bill_form", clear_on_submit=False):
        col1, col2, col3 = st.columns(3)

        with col1:
            bill_no = st.text_input("Bill No.*", value=bill[1] if bill else "", key="bill_no")
            bill_from = st.text_input("Bill From*", value=bill[2] if bill else "", key="bill_from")
            city_from = st.text_input("City From*", value=bill[5] if bill else "", key="city_from")
            quantity = st.number_input("Quantity*", min_value=1, value=int(bill[7]) if bill else 1, key="quantity")

        with col2:
            bill_to = st.text_input("Bill To*", value=bill[3] if bill else "", key="bill_to")
            city_to = st.text_input("City To*", value=bill[6] if bill else "", key="city_to")
            total_amount = st.number_input("Total Amount*", min_value=0.0, value=float(bill[8]) if bill else 0.0, format="%.2f", key="amount")

        with col3:
            product_name = st.text_input("Product Name*", value=bill[4] if bill else "", key="product")
            vehicle_no = st.text_input("Vehicle No.*", value=bill[10] if bill else "", key="vehicle")
            gst_percent = st.number_input("GST Applied (%)", min_value=0.0, max_value=100.0, value=float(bill[9]) if bill else 0.0, format="%.2f", key="gst")

        st.write("")
        col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 4])
        with col_btn1:
            submitted = st.form_submit_button("💾 Submit", use_container_width=True)
        with col_btn2:
            cancel = st.form_submit_button("❌ Cancel", use_container_width=True)

    if submitted:
        # Validate required fields
        if not bill_no or not bill_from or not bill_to or not product_name or not city_from or not city_to or not vehicle_no:
            st.error("⚠️ Please fill all required fields marked with *")
        else:
            data = (bill_no, bill_from, bill_to, product_name, city_from, city_to,
                    quantity, total_amount, gst_percent, vehicle_no)

            try:
                if st.session_state.edit_id:
                    success = db.update_bill(st.session_state.edit_id, data)
                    if success:
                        st.success("✅ Bill updated successfully!")
                        st.session_state.action = None
                        st.session_state.edit_id = None
                        st.rerun()
                else:
                    success = db.create_bill(data)
                    if success:
                        st.success("✅ Bill added successfully!")
                        st.session_state.action = None
                        st.session_state.edit_id = None
                        st.rerun()
            except Exception as e:
                st.error(f"Error saving bill: {e}")

    if cancel:
        st.session_state.action = None
        st.session_state.edit_id = None
        st.rerun()

    st.divider()

# Display bill details if selected
if st.session_state.show_details:
    bill = db.get_bill_by_id(st.session_state.show_details)
    if bill:
        st.subheader("📄 Bill Details")

        # Handle both 11 and 12 column formats
        if len(bill) >= 11:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**ID:** {bill[0]}")
                st.write(f"**Bill No:** {bill[1]}")
                st.write(f"**Bill From:** {bill[2]}")
                st.write(f"**City From:** {bill[5]}")
            with col2:
                st.write(f"**Bill To:** {bill[3]}")
                st.write(f"**City To:** {bill[6]}")
                st.write(f"**Quantity:** {bill[7]}")
                st.write(f"**Vehicle No:** {bill[10]}")
            with col3:
                st.write(f"**Product Name:** {bill[4]}")
                st.write(f"**Total Amount:** ₹{bill[8]:.2f}")
                st.write(f"**GST%:** {bill[9]:.2f}%")
                st.write(f"**Route:** {bill[5]} → {bill[6]}")
                if len(bill) == 12:
                    st.write(f"**Created At:** {bill[11]}")
        col_close1, col_close2 = st.columns([1, 5])
        with col_close1:
            if st.button("✖️ Close Details", use_container_width=True):
                st.session_state.show_details = None
                st.rerun()
        st.divider()
    else:
        st.error("Bill not found!")
        st.session_state.show_details = None
        st.rerun()

# Get all bills
bills = db.get_all_bills()

if bills:
    st.markdown("### 📋 List of E-Way Bills") 
    header_cols = st.columns([0.4, 0.9, 1.2, 1.2, 1.2, 1.3, 0.5, 0.8, 0.6, 1, 1.7])
    headers = ["ID", "Bill No", "From", "To", "Product", "Route", "Qty", "Amount", "GST%", "Vehicle", "Action"]
    for col, header in zip(header_cols, headers):
        with col:
            st.markdown(f"**{header}**")
    st.divider()

    # Data rows
    for bill in bills:
        if len(bill) == 12:
            id_val, bill_no, bill_from, bill_to, product, city_from, city_to, qty, amount, gst, vehicle, created_at = bill
        else:
            id_val, bill_no, bill_from, bill_to, product, city_from, city_to, qty, amount, gst, vehicle = bill

        route = f"{city_from} → {city_to}"
        cols = st.columns([0.4, 0.9, 1.2, 1.2, 1.2, 1.3, 0.5, 0.8, 0.6, 1, 1.7])
        with cols[0]:
            st.write(f"{id_val}")
        with cols[1]:
            st.write(bill_no if bill_no else "-")
        with cols[2]:
            st.write(bill_from if bill_from else "-")
        with cols[3]:
            st.write(bill_to if bill_to else "-")
        with cols[4]:
            st.write(product if product else "-")
        with cols[5]:
            st.write(route)
        with cols[6]:
            st.write(str(qty))
        with cols[7]:
            st.write(f"₹{amount:.2f}")
        with cols[8]:
            st.write(f"{gst:.1f}%")
        with cols[9]:
            st.write(vehicle if vehicle else "-")
        # Action buttons horizontally
        with cols[10]:
            btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])
            with btn_col1:
                if st.button("Read", key=f"read_{id_val}", type="secondary"):
                    st.session_state.show_details = id_val
                    st.session_state.action = None
                    st.session_state.delete_id = None
                    st.rerun()
            with btn_col2:
                if st.button("Edit", key=f"edit_{id_val}", type="secondary"):
                    st.session_state.edit_id = id_val
                    st.session_state.action = "edit"
                    st.session_state.show_details = None
                    st.session_state.delete_id = None
                    st.rerun()
            with btn_col3:
                if st.button("Delete", key=f"delete_{id_val}", type="secondary"):
                    st.session_state.delete_id = id_val
                    st.session_state.show_details = None
                    st.session_state.action = None
                    st.rerun()

        if st.session_state.delete_id == id_val:
            st.warning(f"⚠️ Are you sure you want to delete Bill #{id_val}?")
            conf_col1, conf_col2, conf_col3 = st.columns([1, 1, 8])
            with conf_col1:
                if st.button("✅ Yes", key=f"confirm_delete_{id_val}", use_container_width=True):
                    success = db.delete_bill(id_val)
                    if success:
                        st.success(f"✅ Bill #{id_val} deleted successfully!")
                        st.session_state.delete_id = None
                        st.rerun()
                    else:
                        st.error("Failed to delete bill!")
            with conf_col2:
                if st.button("❌ No", key=f"cancel_delete_{id_val}", use_container_width=True):
                    st.session_state.delete_id = None
                    st.rerun()
        st.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)
else:
    st.info("ℹ️ No bills found. Click 'Add +' to create your first bill.")
