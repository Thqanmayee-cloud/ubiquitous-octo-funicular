import streamlit as st

st.set_page_config(page_title="MiniStore", page_icon="🛍️", layout="wide")

# -----------------------------
# PRODUCTS
# -----------------------------
products = [
    {"name": "Wireless Headphones", "price": 79.99, "desc": "Noise cancelling audio", "cat": "Electronics"},
    {"name": "Smart Watch", "price": 129.99, "desc": "Fitness tracking device", "cat": "Electronics"},
    {"name": "Cotton T-Shirt", "price": 19.99, "desc": "Soft comfortable wear", "cat": "Fashion"},
    {"name": "Leather Backpack", "price": 89.99, "desc": "Stylish travel bag", "cat": "Fashion"},
    {"name": "Coffee Maker", "price": 59.99, "desc": "Fresh coffee at home", "cat": "Home"},
    {"name": "LED Desk Lamp", "price": 34.99, "desc": "Adjustable brightness", "cat": "Home"},
]

st.session_state["products"] = products

# -----------------------------
# CART
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# UI
# -----------------------------
st.title("🛍️ MiniStore")

st.write("Welcome to MiniStore demo e-commerce app!")

st.markdown("---")

st.subheader("⭐ Featured Products")

cols = st.columns(3)

for i, p in enumerate(products):
    with cols[i % 3]:
        st.markdown(f"### {p['name']}")
        st.write(p["desc"])
        st.write(f"Category: {p['cat']}")
        st.write(f"💰 ${p['price']}")

        if st.button("Add to Cart", key=f"cart_{i}"):
            st.session_state.cart.append(p)
            st.success("Added to cart!")
            st.rerun()

# -----------------------------
# SIDEBAR CART
# -----------------------------
st.sidebar.title("🛒 Cart Summary")
st.sidebar.write("Items:", len(st.session_state.cart))
st.sidebar.write("Total:", round(sum(i["price"] for i in st.session_state.cart), 2))

if st.sidebar.button("Clear Cart"):
    st.session_state.cart = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Go to Support Chatbot from sidebar 👈")