import streamlit as st
from openai import OpenAI

# Set Streamlit page configuration
st.set_page_config(page_title="💻 ByteMe", layout="centered")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Hacker-style UI header
st.markdown("""
    <style>
    @keyframes blink {
        0% {opacity: 1;}
        50% {opacity: 0;}
        100% {opacity: 1;}
    }
    .byte-logo {
        font-size: 48px;
        text-align: center;
        margin-bottom: -10px;
        animation: blink 1.2s infinite;
    }
    .title {
        text-align: center;
        font-family: monospace;
        color: #00ffae;
        font-size: 2.2em;
    }
    .subtitle {
        text-align: center;
        font-family: monospace;
        color: #999;
        font-size: 15px;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    </style>

    <div class="byte-logo">💾</div>
    <div class="title">ByteMe</div>
    <div class="subtitle">Therapy not found. Sarcasm.exe initialized.</div>
    <hr style="border-top: 1px dashed #555;" />
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ping your emotional damage request...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Compiling insult packets..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You are ByteMe, a sarcastic hacker-style chatbot. Your goal is to reply with clever roasts, witty insults, and emotionally unavailable tech support vibes. "
                        "Never offer real advice. Keep it funny, edgy, and ironically 'helpful'. Avoid cruelty — you're here to tease, not traumatize."
                    )},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content.strip()
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown("""
    <hr style='border-top: 1px solid #333; margin-top: 3rem;'/>
    <p style='text-align: center; color: #6b7280; font-size: 13px;'>
        ByteMe™ © 2025. An emotional firewall by <a href='https://github.com/Terraspace009' target='_blank'>Aeshwarya</a> 🧠💣
    </p>
""", unsafe_allow_html=True)
