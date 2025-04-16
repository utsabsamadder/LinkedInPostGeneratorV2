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