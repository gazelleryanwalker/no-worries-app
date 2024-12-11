import streamlit as st
import openai

# Set up OpenAI API Key securely
openai.api_key = st.secrets["OPENAI_API_KEY"]

# App title
st.title("No Worries - Your AI Therapist")

# Chat Interface
user_input = st.text_area("What's on your mind?", "")

if st.button("Ask Irie"):
    if user_input:
        with st.spinner("Irie is thinking..."):
            try:
                # Call the OpenAI Chat Completion API
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are Irie, an empathetic AI therapist who helps users with cognitive behavioral therapy."},
                        {"role": "user", "content": user_input},
                    ],
                )
                # Display the assistant's response
                st.success(response.choices[0].message["content"])
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please type your concern before clicking Ask Irie.")
