import streamlit as st
import pandas as pd
from datetime import datetime
from groq import Groq

client = Groq(
    api_key="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",
)

st.title("English Literature Study Assistant")

user_name = st.text_input("Enter your name:")
prompt = st.text_input("Enter a topic or ask a question related to English Literature:")
submit_button = st.button("Get Information")

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ""

def log_user_interaction(user_name, prompt, response):
    log_data = {
        "timestamp": [datetime.now()],
        "user_name": [user_name],
        "question": [prompt],
        "response": [response]
    }
    df = pd.DataFrame(log_data)
    # Append data to CSV file
    df.to_csv("user_interactions.csv", mode='a', header=not pd.io.common.file_exists("user_interactions.csv"), index=False)

if submit_button and user_name and prompt:
    context_prompt = f"You are an experienced English Literature professor. Provide a comprehensive response to the question '{prompt}' for a student named {user_name}. Include detailed explanations, key concepts, important points to remember, notable works and authors related to the topic, summaries, practice questions, and interview questions with answers."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": context_prompt,
            }
        ],
        model="llama3-70b-8192",
    )
    response = chat_completion.choices[0].message.content
    
    # Update chat history
    st.session_state.chat_history += f"\n\n**{user_name}**: {prompt}\n\n**Bot**: {response}"
    
    # Log user interaction
    log_user_interaction(user_name, prompt, response)

# Display chat history
st.text_area("Chat History", value=st.session_state.chat_history, height=400)

if not user_name or not prompt:
    st.write("Please enter both your name and a topic or question to get information.")
