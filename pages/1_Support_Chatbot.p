import streamlit as st

st.set_page_config(page_title="Support Chatbot", page_icon="💬", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

products = st.session_state.get("products", [])
product_names = [p["name"].lower() for p in products]

def bot(msg):
    msg = msg.lower()

    for name in product_names:
        if name in msg:
            return "Yes, that product is available on MiniStore homepage."

    if "delivery" in msg:
        return "Delivery takes 3–5 business days."
    if "refund" in msg:
        return "Refunds are processed in 5–7 days."
    if "return" in msg:
        return "Returns allowed within 7 days."
    if "payment" in msg:
        return "We accept UPI, cards, COD."
    if "order" in msg:
        return "Please share order ID."

    return "Ask about products, delivery, refunds, returns, payments."

st.title("💬 Support Chatbot")

for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])

user = st.chat_input("Ask something...")

if user:
    reply = bot(user)

    st.session_state.chat_history.append({
        "user": user,
        "bot": reply
    })

    st.rerun()