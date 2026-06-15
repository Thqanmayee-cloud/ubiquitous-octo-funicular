import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# PRODUCTS (same shared data)
# -----------------------------
products = st.session_state.get("products", [])

product_names = [p["name"].lower() for p in products]

# -----------------------------
# RULE-BASED CHATBOT LOGIC
# -----------------------------
def bot_response(user_input: str):
    msg = user_input.lower()

    # PRODUCT QUESTIONS
    if any(name in msg for name in product_names):
        return "Yes, that product is available on MiniStore. You can check it on the homepage and add it to cart."

    # DELIVERY
    if "delivery" in msg or "shipping" in msg:
        return "Delivery usually takes 3–5 business days depending on your location."

    # REFUND
    if "refund" in msg:
        return "Refunds are processed within 5–7 working days after approval."

    # RETURNS
    if "return" in msg:
        return "You can return products within 7 days if they are unused and in original packaging."

    # PAYMENT
    if "payment" in msg or "pay" in msg:
        return "We accept UPI, credit/debit cards, and cash on delivery (COD)."

    # ORDER STATUS
    if "order" in msg or "status" in msg:
        return "Please provide your order ID. I will check the status for you."

    # DEFAULT
    return "I'm here to help! Ask me about products, delivery, refunds, returns, or payments."

# -----------------------------
# TITLE
# -----------------------------
st.title("💬 MiniStore Support Chatbot")

st.write("Ask anything about products, orders, delivery, refunds, and more.")

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])

# -----------------------------
# CHAT INPUT
# -----------------------------
user_input = st.chat_input("Type your question...")

if user_input:
    response = bot_response(user_input)

    # store chat
    st.session_state.chat_history.append({
        "user": user_input,
        "bot": response
    })

    # rerun to show updated chat
    st.rerun()