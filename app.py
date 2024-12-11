import streamlit as st
import openai

# OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App Title
st.title("No Worries - Your AI Therapist")

# Initialize session state to track conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are Irie, an empathetic AI therapist who helps with worries."}
    ]

# Display chat history
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.write(f"**Irie:** {message['content']}")

# Input field for new user message
user_input = st.text_input("What's on your mind?", key="user_input")

# Handle user input
if st.button("Ask Irie"):
    if user_input:
        # Add user message to conversation
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Get assistant response from OpenAI
        with st.spinner("Irie is thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=st.session_state["messages"],
                )
                assistant_message = response["choices"][0]["message"]["content"]

                # Add assistant message to conversation
                st.session_state["messages"].append({"role": "assistant", "content": assistant_message})
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please type a message before clicking 'Ask Irie'.")