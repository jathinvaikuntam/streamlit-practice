import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client()

st.title("AI Chatbot")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get new user input
if user_input := st.chat_input("Ask me anything"):

    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Gemini response
    with st.chat_message("assistant"):

        # Convert chat history into a single prompt
        conversation = ""
        for msg in st.session_state.messages:
            conversation += f"{msg['role']}: {msg['content']}\n"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        reply = response.text

        st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )