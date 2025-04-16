# LinkedIn Post Generator

This project is a LinkedIn Post Generator that uses a language model to create posts based on user-defined criteria. The application is built using Python and Streamlit, and it leverages a language model to generate content based on length, language, topic, and custom input.

## Features

- Generate LinkedIn posts with specified length (Short, Medium, Long).
- Choose the language of the post (English or Hinglish).
- Select a topic from predefined tags.
- Provide custom input for additional context or information.
- Uses a language model to generate content based on the provided inputs.

## Project Structure

- `preprocess.py`: Processes raw LinkedIn posts, extracts metadata, and unifies tags.
- `helper_llm.py`: Sets up the language model (LLM) for use in other scripts.
- `post_generator.py`: Generates LinkedIn posts based on specified criteria.
- `few_shot.py`: Manages a collection of processed posts and provides examples for few-shot learning.
- `main.py`: Implements a Streamlit app for generating LinkedIn posts.
- `raw_posts.json`: Contains raw LinkedIn post data.
- `processed_posts.json`: Contains processed LinkedIn post data with metadata.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/utsabsamadder/linkedin-post-generator.git
   cd linkedin-post-generator
2. **Set Up a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

Ensure that langchain_groq and other necessary packages are listed in requirements.txt.

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your API keys for the language models:

   ```bash
   GROQ_API_KEY1=your_groq_api_key_for_llama
   GROQ_API_KEY2=your_groq_api_key_for_whisper
   ```


### Running the Application
1. **Start the Streamlit App**

Run the following command to start the Streamlit application:

    ```bash
    streamlit run main.py
    ```


2. **Interact with the App**
   - Open your web browser and navigate to `http://localhost:8501`.
   - Use the sidebar to select the length, language, and topic for the post.
   - Enter any additional context or information in the custom input text box. 
   - Click the "Generate" button to create a LinkedIn post based on your inputs.



### Troubleshooting
- ModuleNotFoundError: Ensure all dependencies are installed and the virtual environment is activated.
- API Key Issues: Verify that the .env file is correctly set up with your API keys.
### Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Acknowledgments
Thanks to the developers of the language model and Streamlit for providing the tools to build this application.



