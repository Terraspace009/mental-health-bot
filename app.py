import streamlit as st
from openai import OpenAI

<<<<<<< HEAD
# Set page config
st.set_page_config(page_title="Mental Health Support Bot", layout="centered")

# Initialize OpenAI client using the key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Basic emotion detection
=======
# Page config
st.set_page_config(page_title="Dreamy Support Bot", layout="centered")

# OpenAI API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Detect emotion (basic rule-based)
>>>>>>> 54c4a3d (💫 Add dreamy UI to support bot)
def detect_emotion(text):
    emotions = {
        "happy": ["thank", "grateful", "great", "joy", "okay"],
        "sad": ["sad", "cry", "alone", "pain", "depressed"],
        "angry": ["angry", "mad", "hate", "frustrated"],
        "anxious": ["nervous", "worried", "anxious", "panic", "fear"],
    }
    for emotion, words in emotions.items():
        if any(word in text.lower() for word in words):
            return emotion
    return "neutral"

<<<<<<< HEAD
# UI
st.title("🧠 Mental Health Support Bot")
st.markdown("This anonymous AI-powered bot offers emotional support. "
            "Responses are trauma-sensitive and non-judgmental. 💬")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

=======
# Header UI
st.markdown("""
    <h1 style='text-align: center; color: #A78BFA;'>💬 Dreamy Mental Health Support Bot</h1>
    <p style='text-align: center; font-size: 18px; color: #71717A;'>
        Float into a calm space. Type anything — I'm here for you. 🌙
    </p>
    <hr style='border-top: 1px solid #ccc;'/>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
>>>>>>> 54c4a3d (💫 Add dreamy UI to support bot)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
<<<<<<< HEAD
if prompt := st.chat_input("How are you feeling today?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    emotion = detect_emotion(prompt)
    system_instruction = f"You are a kind, trauma-sensitive therapist. The user feels {emotion}. Respond gently and supportively."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt}
        ]
    )

    reply = response.choices[0].message.content
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
=======
if user_input := st.chat_input("💌 How are you feeling today?"):
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    emotion = detect_emotion(user_input)
    sys_prompt = (
        f"You are a soft, dreamy, trauma-sensitive AI friend. "
        f"The user seems to feel '{emotion}'. Respond with warmth, comfort, and a little magic. "
        f"Avoid clinical language. Use comforting tone."
    )

    with st.chat_message("assistant"):
        with st.spinner("Sending gentle thoughts... 🌸"):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": sys_prompt},
                        {"role": "user", "content": user_input}
                    ]
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"⚠️ Error: {e}")

# Footer credit
st.markdown("""
    <hr style='border-top: 1px solid #eee;'/>
    <p style='text-align: center; font-size: 14px; color: #bbb;'>
        Made with 💜 by <a href='https://github.com/Terraspace009' target='_blank'>Aishwarya Shukla</a>
    </p>
""", unsafe_allow_html=True)

>>>>>>> 54c4a3d (💫 Add dreamy UI to support bot)


