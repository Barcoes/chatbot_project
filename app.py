import streamlit as st
import requests
import os

# Retrieve OpenAI API key from Render's environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Make.com Webhook URL
webhook_url = "https://hook.eu2.make.com/l861igtg1gq8x4ckxgcvir24bu31fkbj"

st.title("🚀 Seans Wife Aircraft Manual Cheat Sheet")
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

            # Ensure we received a response
            if response.status_code == 200:
                try:
                    data = response.json()
                    ai_answer = data.get("answer", "No response received.")
                    references = data.get("references", "No references found.")

                    st.write("### 🤖 AI Answer:")
                    st.write(ai_answer)
                    st.write("### 📖 References:")
                    st.write(references)
                
                except ValueError:
                    st.error("Received an invalid response from Make.com. Please check the setup.")
            else:
                st.error(f"Error retrieving response: {response.status_code}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")
