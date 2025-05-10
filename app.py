import streamlit as st
import openai

# Page config
st.set_page_config(page_title="Mental Health Support Bot", layout="centered")

# Load API key securely
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Emotion detection (rule-based)
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

# Title & info
st.title("🧠 Mental Health Support Bot")
st.markdown("This anonymous AI-powered bot offers emotional support. "
            "Responses are trauma-sensitive and non-judgmental. 💬")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("How are you feeling today?")
if prompt:
    user_emotion = detect_emotion(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"You are a trauma-informed therapist. Respond sensitively. The user feels {user_emotion}."},
                        {"role": "user", "content": prompt},
                    ]
                )
                reply = completion.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Something went wrong: {e}")


