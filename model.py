import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

# Function to summarize text
def summarize_text(texts, docsearch, chain):
    try:
        summry = docsearch.similarity_search(" ")
        txt = chain.run(input_documents=summry, question="write summary in points within 150 words")
        return txt
    except Exception as e:
        st.error(f"Error during summarization: {str(e)}")

# Function to answer question
def answer_question(query, docsearch, chain):
    try:
        docs = docsearch.similarity_search(query)
        txt = chain.run(input_documents=docs, question=query)
        return txt
    except Exception as e:
        st.error(f"Error during question answering: {str(e)}")

# Main function
def main():
    st.title('Summarization and Questioning Model')

    api_key = st.text_input('Your OpenAI Key', placeholder="Enter Your key")
    os.environ["OPENAI_API_KEY"] = api_key

    raw_text = ''

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                raw_text += text

    temp_data = st.text_area('Text to analyze', placeholder="Enter Your Data")

    texts = [raw_text]
    if temp_data:
        texts.append(temp_data)

    query = st.text_area('Query on Data', placeholder="Enter Your Query")

    if st.button('Submit') and (uploaded_file is not None or temp_data):
        if api_key == "":
            st.warning('Enter the OpenAI API Key', icon="⚠️")
        else:
            embeddings = OpenAIEmbeddings()
            docsearch = FAISS.from_texts(texts, embeddings)
            chain = load_qa_chain(OpenAI(), chain_type="stuff")

            if query:
                st.write('Output:', answer_question(query, docsearch, chain))
            else:
                st.write('Enter Your Query!')
                st.write('Summary:', summarize_text(texts, docsearch, chain))

if __name__ == '__main__':
    main()
