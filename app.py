import streamlit as st
import openai

# OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("No Worries - Your AI Therapist")

user_input = st.text_area("What's on your mind?")

if st.button("Ask Irie"):
    if user_input:
        with st.spinner("Irie is thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are Irie, an empathetic AI therapist."},
                        {"role": "user", "content": user_input},
                    ],
                )
                st.success(response.choices[0].message["content"])
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please type your concern before clicking Ask Irie.")
