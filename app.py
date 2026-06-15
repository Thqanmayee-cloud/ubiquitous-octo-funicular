import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS (safe styling)
# -----------------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 35px;
    border-radius: 15px;
    color: white;
    text-align: center;
}

.product {
    border: 1px solid #e5e7eb;
    padding: 15px;
    border-radius: 12px;
    background-color: white;
    margin-bottom: 10px;
}

.price {
    color: green;
    font-size: 18px;
    font-weight: bold;
}

.small {
    font-size: 13px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SAMPLE PRODUCTS
# -----------------------------
products = [
    {"name": "Wireless Headphones", "price": 79.99, "desc": "Noise cancelling audio", "cat": "Electronics"},
    {"name": "Smart Watch", "price": 129.99, "desc": "Track fitness easily", "cat": "Electronics"},
    {"name": "Cotton T-Shirt", "price": 19.99, "desc": "Soft comfortable wear", "cat": "Fashion"},
    {"name": "Leather Backpack", "price": 89.99, "desc": "Stylish travel bag", "cat": "Fashion"},
    {"name": "Coffee Maker", "price": 59.99, "desc": "Fresh coffee at home", "cat": "Home"},
    {"name": "LED Desk Lamp", "price": 34.99, "desc": "Bright adjustable light", "cat": "Home"},
]

# -----------------------------
# SESSION CART
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(list(set(p["cat"] for p in products)))
selected_cat = st.sidebar.selectbox("Choose Category", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("Cart Summary")

total_items = len(st.session_state.cart)
total_price = sum(item["price"] for item in st.session_state.cart)

st.sidebar.write("Items:", total_items)
st.sidebar.write("Total: $", round(total_price, 2))

if st.sidebar.button("Clear Cart"):
    st.session_state.cart = []
    st.rerun()

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your modern demo e-commerce store built with Streamlit</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# FILTER PRODUCTS
# -----------------------------
if selected_cat == "All":
    filtered = products
else:
    filtered = [p for p in products if p["cat"] == selected_cat]

# -----------------------------
# FEATURED PRODUCTS
# -----------------------------
st.markdown("## ⭐ Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered):
    with cols[i % 3]:

        st.markdown("### " + product["name"])
        st.markdown(f"<p class='small'>{product['desc']}</p>", unsafe_allow_html=True)
        st.write("Category:", product["cat"])
        st.markdown(f"<p class='price'>${product['price']}</p>", unsafe_allow_html=True)

        if st.button("Add to Cart", key=f"cart_{i}_{product['name']}"):
            st.session_state.cart.append(product)
            st.success("Added to cart!")
            st.rerun()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("© 2026 MiniStore | Streamlit Demo Project")