import streamlit as st
from groq import Groq

client = Groq(
    api_key="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",
)

st.title("English Literature Study Assistant")
prompt = st.text_input("Enter a topic related to English Literature:")
submit_button = st.button("Get Information")

context_prompt = f"You are an experienced English Literature professor. Provide a comprehensive overview of the topic {prompt}. Include the following: an introduction, key concepts, important points to remember, notable works and authors related to the topic, a summary, five practice questions, and ten interview questions with answers."

if submit_button:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": context_prompt,
            }
        ],
        model="llama3-70b-8192",
    )
    st.write(chat_completion.choices[0].message.content)
