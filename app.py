import streamlit as st
import requests
import os

# Retrieve OpenAI API key from Render's environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Make.com Webhook URL (replace with your actual webhook)
webhook_url = "https://hook.make.com/your-unique-webhook-url"

st.title("🚀 Aircraft Manual AI Chatbot")
st.write("Ask me anything about aircraft systems, and I'll find the answers from the manuals.")

# User Input Field
user_question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if user_question.strip():
        try:
            # Send the question to Make.com Webhook
            response = requests.post(
                webhook_url,
                json={"question": user_question}
            )

            # Handle Make.com Response
            if response.status_code == 200:
                data = response.json()
                st.write("### 🤖 AI Answer:")
                st.write(data.get("answer", "No response received."))

                st.write("### 📖 References:")
                st.write(data.get("references", "No references found."))
            else:
                st.error("Error retrieving response. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")
