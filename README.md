DISPLAY 


OVERVIEW: 
This is a Streamlit application for interacting with PDF files. 
It allows users to upload a PDF file and ask questions about its content. 
The application then processes the PDF file, divides it into smaller text chunks, 
and utilizes a language model to generate responses to user questions based on the provided text.

Technologies used:
Python, Streamlit, PyPDF2, langchain, Hugging Face Transformers (specifically google/flan-t5-large).

Main tasks:
User Interface: The code defines a Streamlit user interface for uploading a PDF file and inputting questions. PDF Processing: It extracts text from the uploaded PDF file using PyPDF2 and divides it into smaller chunks. Language Model Interaction: It uses the langchain library and Hugging Face's google/flan-t5-large
model to generate responses to user questions based on the text extracted from the PDF. Displaying Responses: The application displays the generated responses to the user.





