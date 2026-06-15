import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------
st.markdown("""
<style>
    /* Main page styling */
    .main {
        background-color: #f8fafc;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 1.1rem;
    }

    /* Product card */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        height: 280px;
    }

    .product-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #111827;
    }

    .product-price {
        color: #16a34a;
        font-size: 1.1rem;
        font-weight: bold;
        margin-top: 10px;
    }

    .category-badge {
        background-color: #dbeafe;
        color: #1d4ed8;
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        font-size: 0.8rem;
        margin-top: 8px;
    }

    .section-title {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .sidebar-title {
        font-weight: bold;
        font-size: 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sample Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "description": "Premium sound quality with active noise cancellation.",
        "category": "Electronics"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "description": "Track your health, workouts, and daily activity.",
        "category": "Electronics"
    },
    {
        "name": "Classic Cotton T-Shirt",
        "price": 19.99,
        "description": "Comfortable and breathable everyday wear.",
        "category": "Fashion"
    },
    {
        "name": "Leather Backpack",
        "price": 89.99,
        "description": "Stylish backpack for work, travel, and daily use.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 59.99,
        "description": "Brew rich and flavorful coffee in minutes.",
        "category": "Home"
    },
    {
        "name": "Desk Lamp",
        "price": 34.99,
        "description": "Modern LED lamp with adjustable brightness.",
        "category": "Home"
    }
]

# --------------------------------------------------
# Initialize Cart in Session State
# --------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.markdown(
    "<div class='sidebar-title'>🛒 MiniStore Menu</div>",
    unsafe_allow_html=True
)

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

# Shopping Cart Summary
st.sidebar.subheader("Shopping Cart")

cart_count = len(st.session_state.cart)

cart_total = sum(
    item["price"] for item in st.session_state.cart
)

st.sidebar.write(f"Items: **{cart_count}**")
st.sidebar.write(f"Total: **${cart_total:.2f}**")

if st.sidebar.button("Clear Cart"):
    st.session_state.cart = []
    st.rerun()

# --------------------------------------------------
# Homepage Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>
        Your one-stop destination for quality products,
        modern gadgets, fashion essentials, and home accessories.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.markdown(
    "<div class='section-title'>Welcome to MiniStore</div>",
    unsafe_allow_html=True
)

st.write("""
Discover carefully selected products across multiple categories.
Enjoy a clean shopping experience and explore our featured collection below.
""")

# --------------------------------------------------
# Filter Products
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# Featured Products Section
# --------------------------------------------------
st.markdown(
    "<div class='section-title'>Featured Products</div>",
    unsafe_allow_html=True
)

# Create responsive layout using columns
cols_per_row = 3

for i in range(0, len(filtered_products), cols_per_row):
    cols = st.columns(cols_per_row)

    for col, product in zip(cols, filtered_products[i:i+cols_per_row]):
        with col:

            st.markdown(f"""
            <div class="product-card">
                <div class="product-title">
                    {product['name']}
                </div>

                <div class="category-badge">
                    {product['category']}
                </div>

                <p style="margin-top:12px;">
                    {product['description']}
                </p>

                <div class="product-price">
                    ${product['price']:.2f}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"Add to Cart",
                key=product["name"]
            ):
                st.session_state.cart.append(product)
                st.success(
                    f"{product['name']} added to cart!"
                )
                st.rerun()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <center>
        <p>
            © 2025 MiniStore | Demo E-Commerce Website Built with Streamlit
        </p>
    </center>
    """,
    unsafe_allow_html=True
)