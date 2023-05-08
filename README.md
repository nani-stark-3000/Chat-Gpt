# Chat-Gpt

### Introduction

This is a simple Flask-based web application that uses the OpenAI API to generate text-based responses to user prompts. The application provides a web interface that allows users to input a prompt or question, and the ChatGPT model generates a response based on the input.



https://user-images.githubusercontent.com/101336955/236869124-2017df8e-2ca2-4f10-b8de-bf6e692b70c1.mp4



### Prerequisites

To run this application, you will need the following:

- Python 3.x
- Flask framework
- OpenAI API key

### Installation

1. Clone the repository to your local machine.
2. Install the required packages using pip:
   
   ```
   pip install flask
   pip install openai
   ```
   
3. Sign up for an OpenAI API key by following the instructions provided on the OpenAI website: https://beta.openai.com/signup/
4. Once you have obtained an API key, replace the value of the `openai.api_key` variable in the `app.py` file with your API key.
5. Run the application using the following command:

   ```
   python app.py
   ```

   This will start a local development server on port 34.

### Usage

To use the application, navigate to http://localhost:34 in your web browser. You should see a web interface that prompts you to enter a question or prompt. Once you submit your input, the ChatGPT model will generate a response and display it on the web page.

### Limitations

This application is only designed to generate text-based responses to user prompts. It may not work well for more complex tasks or tasks that require visual or audio output.

## Readme

This is a Flask-based web application that uses the OpenAI API to generate text-based responses to user prompts. The application provides a simple web interface that allows users to input a prompt or question, and the ChatGPT model generates a response based on the input.

To use the application, follow the installation and usage instructions provided in the documentation.

Please note that this application is intended for educational and experimental purposes only. The use of the OpenAI API is subject to the OpenAI terms of service, and users should be aware of any applicable usage limits or restrictions.
