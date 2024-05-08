import os
import pickle
import time
import requests
from io import BytesIO
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate, LLMChain, HuggingFaceHub
import streamlit as st
from ui import show_upload_ui, show_query_input

TEMPLATE = """ 
Given the provided {text}, 
proceed to answer the user's question: "{question}" 
and provide the best response possible. 
Please adhere to the provided text to generate the most comprehensive and stable answer. 
If unable to find the answer, respond with "No matching data." 
Please refrain from creating incorrect answers when no matching data is found.

"""
prompts = PromptTemplate(input_variables=["text", "question"], template=TEMPLATE)


def process_pdf(pdf):
    if pdf is not None:
        pdf_bytes = pdf.read()  # Read the bytes of the uploaded PDF
        pdf_reader = PdfReader(BytesIO(pdf_bytes))  # Create a PdfReader object from the bytes
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)
        return chunks
    else:
        return []

def main():
    pdf = show_upload_ui()
    api_query = show_query_input()

    if pdf:
        chunks = process_pdf(pdf)
        if api_query:
            responses = []
            chain = LLMChain(llm=HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={'temperature': 0.1}, huggingfacehub_api_token="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"), prompt=prompts)

            for chunk in chunks:
                if chunk.strip():  # Check if the chunk is not empty
                    result = chain.run({
                        "text": chunk,
                        "question": api_query
                    })
                    responses.append(result)
            
            st.write("Answers:")
            for response in responses:
                st.write(response)
               
        

        
if __name__ == '__main__':
    main()
