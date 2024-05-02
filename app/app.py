import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


def get_response(user_input):
    return "I am a bot"


def main():
    st.set_page_config(page_title="Chat with Medium", page_icon=":robot:")
    st.title("Chat with Medium")
    
    with st.sidebar:
        website_url = st.text_input("**Website URL**", "https://medium.com/")
    

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage("Hello! I am a bot. How can I help you?"),
        ]

    user_query = st.chat_input("Type a message...", key="input")

    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(user_query))
        bot_response = get_response(user_query)
        st.session_state.chat_history.append(AIMessage(bot_response))
        
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write("AQChat:", message.content)
        else:
            with st.chat_message("User"):
                st.write("User: ", message.content)


if __name__ == "__main__":
    main()
