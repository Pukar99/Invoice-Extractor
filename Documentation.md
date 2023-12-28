# Documentation

## Overview

`app.py` is a Q&A Chatbot designed for reading and interpreting reception bills. The application utilizes the `langchain.llms` module for OpenAI, Streamlit for user interface, and Google's generative AI for image processing and response generation.

## Dependencies

- `dotenv`: Loads environment variables from a `.env` file.
- `streamlit`: Powers the web interface of the application.
- `os`: Provides a way to use operating system dependent functionality.
- `pathlib`: Offers an object-oriented interface for working with filesystem paths.
- `textwrap`: Helps in formatting text.
- `PIL`: Python Imaging Library for opening, manipulating, and saving many different image file formats.
- `google.generativeai`: Used to access Google's generative AI capabilities.

## Configuration and Setup

### Environment Variables

- The application retrieves the Google API key from environment variables using `dotenv`.

### Google API Configuration

- Configures the Google generative AI module using the API key.

## Core Functionality

### Image Upload and Processing

- Users can upload reception bill images in JPG, JPEG, or PNG formats.
- Uploaded images are processed to extract data for analysis.

### Generating Responses

- The application uses Google's `gemini-pro-vision` model to generate responses based on the uploaded image and user input.

### Streamlit UI Components

- `st.set_page_config`: Sets the page configuration for the Streamlit app.
- `st.header`, `st.subheader`, `st.text_input`, `st.file_uploader`, `st.button`, and `st.write`: These are used to create the interactive components of the web interface.

### Bill Analysis

- Upon clicking the 'Analyze the Bill' button, the application:
  - Processes the uploaded image.
  - Sends the image along with the input prompt to the `gemini-pro-vision` model.
  - Displays the analysis result on the Streamlit interface.

## Error Handling

- The application raises a `FileNotFoundError` if no file is uploaded when the 'Analyze the Bill' button is pressed.

## Usage

- The user provides a prompt and uploads a reception bill image.
- Clicking the 'Analyze the Bill' button initiates the analysis.
- The response from the AI model is displayed as the analysis result.
