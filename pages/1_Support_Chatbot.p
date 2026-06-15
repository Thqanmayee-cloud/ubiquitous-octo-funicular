import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Support Chatbot", page_icon="💬", layout="wide")

# -----------------------------
# OPENAI CLIENT
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# GET PRODUCTS FROM HOME
# -----------------------------
products = st.session_state.get("products", [])

product_text = "\n".join(
    [f"- {p['name']} (${p['price']}): {p['desc']}" for p in products]
)

# -----------------------------
# SYSTEM PROMPT
# -----------------------------
SYSTEM_PROMPT = f"""
You are MiniStore customer support assistant.

You ONLY answer:
- products
- delivery
- refunds
- returns
- payments
- order issues

Rules:
- Be polite and professional
- If question is unrelated, say:
"I can only help with MiniStore support."

Products:
{product_text}
"""

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💬 MiniStore Support Chatbot")

st.write("Ask anything about MiniStore products or orders.")

# -----------------------------
# SHOW CHAT
# -----------------------------
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# INPUT
# -----------------------------
user_input = st.chat_input("Type your question...")

if user_input:
    st.chat_message("user").write(user_input)

    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *st.session_state.chat_history
        ]
    )

    reply = response.choices[0].message.content

    st.chat_message("assistant").write(reply)

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": reply
    })