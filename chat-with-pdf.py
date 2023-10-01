import tempfile
from PIL import Image
import os
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import streamlit as st 
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import *
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.agents.agent_toolkits import *
import base64
from gtts import gTTS
from io import BytesIO
from pygame import mixer
import tiktoken
import chromadb
from langchain.text_splitter import TokenTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
st.title("📄 Chat and Listen PDF 🤖") # Title of the app
st.write("I will build a conversational AI bot right on the fly from the PDF provided by you. Just upload the PDF and I will learn from it. Then you can ask me anything and I will answer you.")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()) # Encodes the image to base 64
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()}); # Adds the background image to the app
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True # Allows the HTML code to be displayed
    )
#add_bg_from_local('page.png')    # Calls the function to add the background image
st.sidebar.title("Give me the PDF to learn") # Title of the sidebar
upload=st.sidebar.file_uploader("Upload your PDF",type=['pdf']) # File uploader
if upload is not None:
    tdir=tempfile.TemporaryDirectory()  # Temporary directory to store the uploaded file
    tpath=os.path.join(tdir.name,'file.pdf') 
    with open(tpath,'wb') as f:
        f.write(upload.getbuffer()) # Writes the uploaded file to the temporary directory
    st.sidebar.write("Uploaded")
    st.sidebar.write("Now I will learn from it") # Message to be displayed after the file is uploaded


# os.environ['OPENAI_API_KEY']

model=OpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"],model="gpt-3.5-turbo") # Model to be used for the bot. You can change it to any other model from the list of models supported by OpenAI to get different results.
emb=OpenAIEmbeddings(openai_api_key=st.secrets["OPENAI_API_KEY"])  # Embeddings to be used for the bot.
load=PyPDFLoader(tpath) # Loader to load the PDF file
pages=load.load()      # Loads the PDF file
splitter=TokenTextSplitter(chunk_size=1000,chunk_overlap=0)
split_data=splitter.split_documents(pages)    # Splits the PDF file into chunks of 1000 tokens each
collection_name='CC_collection'     # Name of the collection
local_directory = "CC_dir"         # Directory to store the collection
persist_directory = os.path.join(os.getcwd(), local_directory)
vectDB = Chroma.from_documents(split_data,
                      emb,
                      collection_name=collection_name,
                      persist_directory=persist_directory
                      )              # Creates the vector database from the PDF file and stores it in the local directory
vectDB.persist()      # Persists the vector database
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True) # Creates a memory for the bot to remember the conversation
chatQA = ConversationalRetrievalChain.from_llm(
            OpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"],
               temperature=0, model_name="gpt-3.5-turbo"), 
            vectDB.as_retriever(), 
            memory=memory)               # Creates the bot

chat_history=[]
prompt=st.text_input("Enter your prompt")      # Takes the prompt from the user
if prompt:
        with st.spinner('Generating response...'):                   
            response = chatQA({"question": prompt+"limit your answer to less than 50 words" ,"chat_history":chat_history}, return_only_outputs=True) # Generates the response from the bot
            answer = response['answer']
            st.write(answer)        # Displays the response
            myobj = gTTS(text=answer,lang='en', slow=False)     # Converts the response to speech
            mp3_play=BytesIO()         # Creates a BytesIO object
            myobj.write_to_fp(mp3_play)
            st.audio(mp3_play,format="audio/mp3")      # Plays the audio
else:
            st.warning('Please enter your prompt')
