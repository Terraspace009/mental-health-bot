# ByteMe 🤖💔  
### *Your emotionally unstable, sarcastic AI companion... with feelings, sometimes.*

---

## 🧠 About the Project

ByteMe is a trauma-aware chatbot that blends emotional intelligence with dark humour. Built as a mental health tech parody, it detects user emotion, responds with context-aware prompts, and keeps things... just unhinged enough. Think: OpenAI meets Kuromi with a keyboard.

---

## 🧰 Tech Stack

- **Python + Streamlit**  
- **OpenAI GPT API**  
- **NRC Emotion Lexicon for Emotion Detection**  
- **Custom Kuromi-inspired UI with animation**  
- **Heroku / Streamlit Cloud (for deployment)**

---

## 💡 Features

- 🎭 Emotion detection from user input  
- 🤬 Sarcastic + empathetic mixed response logic  
- 🎨 Animated UI with themed fonts and icons  
- 🧵 Chat log with mood coloring  
- 🌐 Ready for web deployment

---

## 🧩 How It Works

## 🧩 How It Works

```mermaid
graph TD;
    UserInput --> EmotionDetector
    EmotionDetector --> GPTResponse
    GPTResponse --> StreamlitUI
    StreamlitUI --> ResponseDisplay


git clone https://github.com/Terraspace009/ByteMe.git
cd ByteMe

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
