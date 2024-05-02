import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Chat Interface",
    layout="wide",
    page_icon=":speech_balloon:",
)

# Sidebar with title and optional content
st.sidebar.title("Chat Interface")
st.sidebar.write("This is a basic chat interface.")


# Chatbot logic (in a real-world scenario, this would involve a backend AI model)
def simple_bot_response(user_input):
    # Basic example: Echo the user input
    return f"You said: '{user_input}'"


# Container for the chat interface
chat_container = st.container()

# Session state to store the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Form for user input
with chat_container:
    with st.form("chat_form"):
        user_input = st.text_input(
            "Type your message here...", key="user_input", max_chars=500
        )
        submit_button = st.form_submit_button(label="Send")

        if submit_button and user_input:
            # Append user message to chat history
            st.session_state.chat_history.append(
                {"sender": "user", "message": user_input, "time": datetime.now()}
            )

            # Generate bot response and append it to chat history
            bot_response = simple_bot_response(user_input)
            st.session_state.chat_history.append(
                {"sender": "bot", "message": bot_response, "time": datetime.now()}
            )

# Display chat history
for entry in st.session_state.chat_history:
    sender = "User" if entry["sender"] == "user" else "Bot"
    message = entry["message"]
    time = entry["time"].strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"**{sender}** [{time}]: {message}")

# Make the chat interface full width and full height
st.markdown("<style>body { margin:0; padding:0; }</style>", unsafe_allow_html=True)
