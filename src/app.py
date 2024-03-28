#  pip install streamlit langchain langchain-openai

import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "I don't know "



# app config
st.set_page_config(page_title="Chat With Websites",page_icon="🤖")
st.title("Chat With Websites")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a bot, How can I help you ? ")

    ]

# sidebar
with st.sidebar:
    st.header("settings")
    website_URL=st.text_input("Website URL")

#  disable conversion until website url is not given 

if website_URL is None or website_URL == "":
    st.info("Please enter a website URL ")
else:
    # user input 
    user_query=st.chat_input("Type Your Message Here...")
    if user_query is not None and user_query !="":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))


    #  conversion
            
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)



        # with st.chat_message("Human"):
        #     st.write(user_query)

        # with st.chat_message("AI"):
        #     st.write(response)

        # with st.sidebar:
        #     st.write(st.session_state.chat_history)



