import streamlit as st

st.set_page_config(page_title="Support Chatbot", page_icon="💬", layout="wide")

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# PRODUCTS FROM HOMEPAGE
# -----------------------------
products = st.session_state.get("products", [])
product_names = [p["name"].lower() for p in products]

# -----------------------------
# BOT LOGIC
# -----------------------------
def bot_reply(msg):
    msg = msg.lower()

    # product detection
    for name in product_names:
        if name in msg:
            return "Yes 👍 that product is available in MiniStore."

    if "delivery" in msg or "shipping" in msg:
        return "Delivery takes 3–5 business days."

    if "refund" in msg:
        return "Refunds are processed within 5–7 days."

    if "return" in msg:
        return "You can return items within 7 days if unused."

    if "payment" in msg:
        return "We accept UPI, cards, and COD."

    if "order" in msg or "status" in msg:
        return "Please share your order ID."

    return "Ask about products, delivery, refunds, returns, payments, or orders."

# -----------------------------
# TITLE
# -----------------------------
st.title("💬 Support Chatbot")

st.write("Ask anything about MiniStore")

# -----------------------------
# CHAT DISPLAY
# -----------------------------
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])

# -----------------------------
# INPUT
# -----------------------------
user_input = st.chat_input("Type your question...")

if user_input:
    response = bot_reply(user_input)

    st.session_state.chat_history.append({
        "user": user_input,
        "bot": response
    })

    st.rerun()