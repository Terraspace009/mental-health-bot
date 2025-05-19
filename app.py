import streamlit as st
from openai import OpenAI

# Set page config at the very top
st.set_page_config(page_title="💀 Dark Humour Bot", layout="centered")

# OpenAI setup
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Header
st.markdown("""
    <h1 style='text-align: center; color: #ec4899;'>💀 Dark Humour Bot</h1>
    <p style='text-align: center; color: #cbd5e1; font-size: 18px;'>
        Got a problem? I'm not here to help — just to roast it with style.<br>
        Sarcasm, cynicism, and existential dread served fresh. 🖤
    </p>
    <hr style='border-top: 1px dashed #4b5563;'/>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("How shall I roast your misery today?")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate dark response
    with st.chat_message("assistant"):
        with st.spinner("Sharpening sarcasm..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a dark humour assistant. Be witty, cynical, sarcastic, and blunt — never helpful."},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown("""
    <hr style='border-top: 1px solid #333; margin-top: 3rem;'/>
    <p style='text-align: center; color: #6b7280; font-size: 13px;'>
        Built for laughs, not therapy. © 2025 <a href='https://github.com/Terraspace009' target='_blank'>Aeshwarya S</a>
    </p>
""", unsafe_allow_html=True)
