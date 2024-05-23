import streamlit as st
from groq import Groq

client = Groq(
    api_key="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",
)

st.title("LLM and Python Study Assistant")
prompt = st.text_input("Enter a topic related to Language Models (LLM) or Python:")
submit_button = st.button("Get Information")

context_prompt = f"You are an AI tutor specializing in Language Models and Python programming. Provide a comprehensive overview of the topic {prompt}. Include the following: an introduction, key concepts, technical details, practical applications, ethical considerations (if applicable), practical implementation with code examples, additional resources for further learning, and common questions and troubleshooting tips."

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
