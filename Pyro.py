import streamlit as st
from groq import Groq

client = Groq(
    api_key="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",
)

st.title("Pyro_coder")
prompt= st.text_input("Get detailed docs on anything Python:")
submit_button = st.button("Jaldi Bata")
context_prompt = f"Act as an experienced technical trainer, who focuses in python and machine learning, give proper definitions, points to remember, code examples, summary, five practice questions and 10 interview questions and answers  on the topic  {prompt}"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": context_prompt,
        }
    ],
    model="llama3-70b-8192",
)

if submit_button:
    st.write(chat_completion.choices[0].message.content)