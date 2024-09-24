import google.generativeai as genai
import streamlit as st

# Configure Google API key
GOOGLE_API_KEY = "AIzaSyD1GBRvNeyNMS9ywWtjLynSvmdOmK4MjCA"

genai.configure(api_key=GOOGLE_API_KEY)

# Initilize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Define a function to get response from model
def get_chatbot_response(user_input):
    respnse = model.generate_content(user_input)
    return respnse.text


st.title(" 🌟 Simple ChatBot 🌟 ")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []


    
    # Custom CSS for styling
st.markdown("""
    <style>
    .chat-container {
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f7f7f7;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .chat-header {
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        color: #333;
        text-align: center;
        margin-bottom: 10px;
    }
    .chat-box {
        display: flex;
        flex-direction: column;
        margin-top: 20px;
    }
    .user-message, .bot-message {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        width: fit-content;
    }
    .user-message {
        background-color: #dcf8c6;
        align-self: flex-end;
        color: #000;
    }
    .bot-message {
        background-color: #fff;
        align-self: flex-start;
        color: #000;
        border: 1px solid #ccc;
    }
    .submit-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        cursor: pointer;
    }
    .submit-btn:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)


# user_input = input("Enter your Prompt : ")
# output = getResponseFromModel(user_input)

# print(output)


with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
            st.write(response)
        else:
            st.warning("Please enter a prompt.")