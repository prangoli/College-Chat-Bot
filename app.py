from bot import ChatBot
import streamlit as st
import re

bot = ChatBot()
    
st.set_page_config(page_title="Professional Seminar II Bot")
with st.sidebar:
    st.title('Professional Seminar II Bot')


def extract_answer(text):
    match = re.search(r'Answer:\s*(.*)', text, re.DOTALL)
    if match:
        answer = match.group(1).strip()
        return answer
    else:
        return text  


def generate_response(input):
    result = bot.rag_chain.invoke(input)
    return extract_answer(result)


if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, let's pass this insufferable subject"}]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Analyzing class notes.."):
            response = generate_response(input) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
