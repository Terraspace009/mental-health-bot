import streamlit as st
import openai

# Set Streamlit page configuration
st.set_page_config(page_title="Dark Humour Bot", layout="centered")

# Load API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Title and description
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4;'>💀 Dark Humour Bot</h1>
    <p style='text-align: center; font-size: 18px; color: #bbb;'>
        Got a problem? I'm not here to help — just to roast it with style.<br>
        Sarcasm, cynicism, and existential dread served fresh. 🖤
    </p>
    <hr style='border-top: 1px dashed #666;'/>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input field
user_input = st.chat_input("Drop your darkest thought...")

if user_input:
    # Display user's message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate GPT response
    with st.chat_message("assistant"):
        with st.spinner("Cooking up something rude..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You're a dark humour AI chatbot. "
                        "Reply with witty, sarcastic, or ironic comebacks. "
                        "Use dry humour and cynicism. Do not give therapy advice. "
                        "Avoid being cruel or offensive — just clever and darkly funny."
                    )},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# Footer
st.markdown("""
    <hr style='border-top: 1px dashed #999;'/>
    <p style='text-align: center; font-size: 13px; color: #666;'>
        This bot is 92% sarcasm and 8% caffeine.<br>
        Built by <a href='https://github.com/Terraspace009' target='_blank'>Aishwarya </a> 🖤
    </p>
""", unsafe_allow_html=True)


