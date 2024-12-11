import streamlit as st
import openai

# Set up the OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title
st.title("No Worries - Your AI Therapist")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Irie, an empathetic AI therapist who helps teenagers manage their worries using CBT techniques. Always respond with compassion, reassurance, and actionable advice to address their concerns."}
    ]

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.write(f"**Irie:** {message['content']}")

# User input
user_input = st.text_input("What's on your mind?", key="input")

if st.button("Ask Irie"):
    if user_input:
        # Add user input to messages
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Call OpenAI API
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.messages,
            )
            assistant_message = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        except Exception as e:
            st.error(f"Error: {e}")

        # Clear the input box
        st.session_state["input"] = ""

# Save chat history
st.write("---")
st.subheader("Chat History")
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.write(f"**Irie:** {message['content']}")