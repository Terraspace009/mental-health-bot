import streamlit as st
from openai import OpenAI

# Set page config
st.set_page_config(page_title="Mental Health Support Bot", layout="centered")

# Initialize OpenAI client using the key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Basic emotion detection
def detect_emotion(text):
    emotions = {
        "happy": ["thank", "grateful", "great", "joy"],
        "sad": ["sad", "cry", "alone", "pain", "depressed"],
        "angry": ["angry", "mad", "hate", "frustrated"],
        "anxious": ["nervous", "worried", "anxious", "panic", "fear"],
    }
    for emotion, keywords in emotions.items():
        for word in keywords:
            if word in text.lower():
                return emotion
    return "neutral"

# UI
st.title("🧠 Mental Health Support Bot")
st.markdown("This anonymous AI-powered bot offers emotional support. "
            "Responses are trauma-sensitive and non-judgmental. 💬")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
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


