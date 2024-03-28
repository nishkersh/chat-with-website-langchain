#  pip install streamlit langchain langchain-openai beautifulsoup4 python-dotenv

import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_response(user_input):
    return "I don't know "

def get_vectorstore_from_url(url):
    # get the textin document form 
    loader = WebBaseLoader(url)
    document = loader.load()

    #  split the document into cbunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # create vectorstore from the chunks
    vector_store = Chroma.from_documents(document_chunks, OpenAIEmbeddings() )

    return vector_store

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
    document_chunks = get_vectorstore_from_url(website_URL)
    
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



