# Q&A chatbot
# from langchain.llms import Openai
import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown





def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text ,">", predicate=lambda _: True))

## Function to load OpenAI model and get respones

from dotenv import load_dotenv

load_dotenv() #take env variable from .env

API_Key  = os.getenv("GOOGLE_GEMINI_API")
genai.configure(api_key=API_Key)

def get_gemini_reponse(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if button is clicked

if submit:

    response = get_gemini_reponse(input)
    st.subheader("The Response is")
    st.write(response)