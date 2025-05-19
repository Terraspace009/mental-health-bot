import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(page_title="💀 Kuromi Bot", layout="centered")

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Kuromi styling + header
st.markdown("""
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .kuromi-icon {
        width: 80px;
        display: block;
        margin: 0 auto;
        animation: spin 4s linear infinite;
        margin-bottom: 10px;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        color: #ff69b4;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .subtitle {
        text-align: center;
        color: #d4a5ff;
        font-size: 16px;
        margin-top: -10px;
    }
    </style>

    <img src="https://media.tenor.com/8NU1WJmYp-0AAAAi/kuromi-rotate.gif" class="kuromi-icon" />
    <h1 class='title'>💀 Kuromi Bot</h1>
    <p class='subtitle'>Cute, chaotic, and full of sass. Drop your drama — I’ll roast it with style.</p>
    <hr style='border-top: 1px dashed #888;'/>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your tragic tale...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Summoning Kuromi sass..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You're a dark humour chatbot inspired by Kuromi — sarcastic, stylish, playful, and edgy. "
                        "Roast the user gently. Be dark but never cruel. Think glitter and doom in equal parts."
                    )},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content.strip()
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown("""
    <hr style='border-top: 1px solid #555; margin-top: 3rem;'/>
    <p style='text-align: center; font-size: 13px; color: #999;'>
        🖤 Powered by sarcasm, glitter, and caffeine.<br>
        Made with chaos by <a href='https://github.com/Terraspace009' target='_blank'>Aeshwarya</a>
    </p>
""", unsafe_allow_html=True)
