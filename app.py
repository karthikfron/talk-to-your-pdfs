import streamlit as st

from dotenv import load_dotenv

from PyPDF2 import PdfReader

from langchain.text_splitter import CharacterTextSplitter

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from htmltemp import css,bot_template,user_template

from langchain.llms import HuggingFaceHub





def get_pdf_text(pdf_docs):
   text=""  #we initialize var called text in which we store all text from pdf
   for pdf in pdf_docs: #looping through each pdf
      pdf_reader=PdfReader(pdf)    
      for page in pdf_reader.pages: #loop through all pages
         text+= page.extract_text()  #extracted and conct to text 
   return text


def get_text_chunks(text):
  text_splitter=CharacterTextSplitter(
      separator="\n",
      chunk_size=1000, #means 1000 characters
      chunk_overlap=200,
      length_function=len

   )

  chunks=text_splitter.split_text(text)
  return chunks
   
   
def get_vector_store(text_chunks):
   embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
   vectorestore=FAISS.from_texts(texts=text_chunks,embedding=embeddings)
   return vectorestore
   
   
def get_convesation_chain(vectorestore):
   memory=ConversationBufferMemory(memory_key='chat_history',return_messages=True)
   llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None
    )
   conversation_chain=ConversationalRetrievalChain.from_llm(
      llm=llm,
      retriever=vectorestore.as_retriever(),
      memory=memory
      

   )
   return conversation_chain
   

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiplr PDFs",page_icon=":bike:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
  

    st.header("Chat with multiplr PDFs :bike:")
    user_question= st.text_input("Ask a question about your Documents:")

    if user_question:
        handle_userinput(user_question)

   
    with st.sidebar:
       st.subheader("Your document")
       pdf_docs= st.file_uploader("Uplaod your PDF's here and click on 'Process",accept_multiple_files=True)
       if st.button("Process") :
          with st.spinner("Processing"):
          

             #get pdf text raw cont of pdf
             raw_text =get_pdf_text(pdf_docs)
          #  st.write(raw_text)



        
          #get text chunks 
             text_chunks=get_text_chunks(raw_text)
          # st.write(text_chunks)



         # create vector store
             vectorstore = get_vector_store(text_chunks)

         # create conversation chain
             st.session_state.conversation = get_convesation_chain(
                    vectorstore)
     
    

if __name__=='__main__':
 main()