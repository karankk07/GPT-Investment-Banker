# Import os to set API key
import os
#Import OpenAI as main LLM service
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
# birng in streamlit for UI/app interface
import streamlit as st

# Import PDF doc loaders 
from langchain.document_loaders import PyPDFLoader
# Import chroma as the vector store
from langchain.vectorstores import Chroma

# Import vector store stuff
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

#set APIkey for OpenAI service
os.environ['OPENAI_API_KEY']= 'yourapikeyhere'

llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()

# create and load PDF loader
loader = PyPDFLoader('annualreport.pdf')
# split pages from pdf
pages = loader.load_and_split()
# load doc into vector database aka ChromaDB
store = Chroma.from_documents(pages, collection_name= 'annualreport')

# create vectorstore info obj
vectorstore_info = VectorStoreInfo(
    name = "annual_report",
    description = "a bank annual report as a pdf",
    vectorstore = store
)

# convert the doc stored into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info= vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit= toolkit,
    verbose = True
)

st.title('🦜🔗 GPT Investment Banker')
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')

#If the user hits enter
if prompt:
    # swap out the raw llm for a document agent
    response = agent_executor.run(prompt)
    # write it out to the screen
    st.write(response)

    # with a streamlit expander
    with st.expander('Document Similiarity search'):
        # Find the relevent pages
        search = store.similarity_search_with_score(prompt)
        # Write out the first 
        st.write(search[0][0].page_content)