# Q&A Chatbot for Reception Bill Reading
#from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {"mime_type": uploaded_file.type, "data": bytes_data}
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our streamlit app
st.set_page_config(page_title="Reception Bill Reader")

st.header("Reception Bill Analysis Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Upload a reception bill image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Bill Image.", use_column_width=True)

submit = st.button("Analyze the Bill")

input_prompt = """
               You are an expert in understanding and analyzing reception bills.
               You will receive input images as reception bills and
               you will have to extract and interpret information based on these images.
               """

# If the analyze button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Analysis Result")
    st.write(response)

