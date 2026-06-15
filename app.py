import streamlit as st

st.set_page_config(page_title="MiniStore", page_icon="🛍️", layout="wide")

# -----------------------------
# PRODUCTS (shared with chatbot)
# -----------------------------
products = [
    {"name": "Wireless Headphones", "price": 79.99, "desc": "Noise cancelling audio", "cat": "Electronics"},
    {"name": "Smart Watch", "price": 129.99, "desc": "Track fitness easily", "cat": "Electronics"},
    {"name": "Cotton T-Shirt", "price": 19.99, "desc": "Soft comfortable wear", "cat": "Fashion"},
    {"name": "Leather Backpack", "price": 89.99, "desc": "Stylish travel bag", "cat": "Fashion"},
    {"name": "Coffee Maker", "price": 59.99, "desc": "Fresh coffee at home", "cat": "Home"},
    {"name": "LED Desk Lamp", "price": 34.99, "desc": "Bright adjustable light", "cat": "Home"},
]

st.session_state["products"] = products

if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# UI
# -----------------------------
st.markdown("<h1 style='text-align:center;'>🛍️ MiniStore</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Simple Demo E-Commerce App</p>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("⭐ Featured Products")

cols = st.columns(3)

for i, p in enumerate(products):
    with cols[i % 3]:
        st.markdown(f"### {p['name']}")
        st.write(p["desc"])
        st.write("Category:", p["cat"])
        st.write(f"💰 ${p['price']}")

        if st.button("Add to Cart", key=f"cart_{i}"):
            st.session_state.cart.append(p)
            st.success("Added!")
            st.rerun()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🛒 Cart")
st.sidebar.write("Items:", len(st.session_state.cart))
st.sidebar.write("Total:", round(sum(i["price"] for i in st.session_state.cart), 2))

if st.sidebar.button("Clear Cart"):
    st.session_state.cart = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Go to Support Chatbot from sidebar 👈")p