import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="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")

# Streamlit app
def main():
    st.title("Chat with K")
    
    # Input prompt from user
    prompt = st.text_input("Enter your prompt:")
    
    if st.button("Submit"):
        if prompt:
            # Send prompt to Groq for completion
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="mixtral-8x7b-32768",
            )
            # Display AI response
            st.write("AI Response:")
            response = chat_completion.choices[0].message.content
            st.write(response)
            
            # Save response to a text file
            save_as_text_file(response)
        else:
            st.warning("Please enter a prompt.")

def save_as_text_file(response):
    with open("ai_response.txt", "w") as file:
        file.write(response)
    st.success("AI response saved as ai_response.txt")

if __name__ == "__main__":
    main()
