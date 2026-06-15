import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="MiniStore", layout="wide")

# -----------------------------
# CSS (safe usage)
# -----------------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 30px;
    border-radius: 12px;
    color: white;
    text-align: center;
}

.product-box {
    border: 1px solid #e5e7eb;
    padding: 15px;
    border-radius: 10px;
    background-color: white;
}
.price {
    color: green;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sample Products
# -----------------------------
products = [
    {"name": "Wireless Headphones", "price": 79.99, "desc": "Noise cancelling sound", "cat": "Electronics"},
    {"name": "Smart Watch", "price": 129.99, "desc": "Track fitness easily", "cat": "Electronics"},
    {"name": "Cotton T-Shirt", "price": 19.99, "desc": "Soft and comfortable", "cat": "Fashion"},
    {"name": "Leather Backpack", "price": 89.99, "desc": "Stylish and durable", "cat": "Fashion"},
    {"name": "Coffee Maker", "price": 59.99, "desc": "Fresh coffee at home", "cat": "Home"},
    {"name": "LED Desk Lamp", "price": 34.99, "desc": "Bright adjustable light", "cat": "Home"},
]

# -----------------------------
# Session Cart
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(list(set(p["cat"] for p in products)))
choice = st.sidebar.selectbox("Category", categories)

st.sidebar.subheader("Cart")
st.sidebar.write("Items:", len(st.session_state.cart))
st.sidebar.write(
    "Total: $",
    round(sum(i["price"] for i in st.session_state.cart), 2)
)

if st.sidebar.button("Clear Cart"):
    st.session_state.cart = []
    st.rerun()

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>MiniStore 🛍️</h1>
    <p>Your modern demo shopping app</p>
</div>
""", unsafe_allow_html=True)

st.write("### Featured Products")

# -----------------------------
# Filter Products
# -----------------------------
filtered = products if choice == "All" else [p for p in products if p["cat"] == choice]

# -----------------------------
# PRODUCT DISPLAY (FIXED)
# -----------------------------
cols = st.columns(3)

for idx, product in enumerate(filtered):
    with cols[idx % 3]:
        with st.container():
            st.markdown("### " + product["name"])
            st.write(product["desc"])
            st.markdown(f"**Category:** {product['cat']}")
            st.markdown(f"<p class='price'>${product['price']}</p>", unsafe_allow_html=True)

            if st.button("Add to Cart", key=product["name"]):
                st.session_state.cart.append(product)
                st.success("Added to cart!")
                st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("© MiniStore Demo App")
)