import streamlit as st
import openai

# Set page configuration
st.set_page_config(page_title="Mental Health Support Bot", layout="centered")

# Load your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Basic rule-based emotion detection
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

# UI header
st.title("🧠 Mental Health Support Bot")
st.markdown("This anonymous AI-powered bot offers emotional support. "
            "Responses are trauma-sensitive and non-judgmental. 💬")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown

