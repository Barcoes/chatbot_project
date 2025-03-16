import streamlit as st
import openai
import os

# Retrieve API key from Render's environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Ensure API key is set
if not api_key:
    st.error("API key is missing! Please check Render's environment settings.")
else:
    openai.api_key = api_key

st.title("AI Chatbot")

user_input = st.text_input("Ask a question:")

if user_input:
    try:
        # Correct OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract AI response
        ai_reply = response["choices"][0]["message"]["content"]

        st.write(ai_reply)

    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API error: {str(e)}")
