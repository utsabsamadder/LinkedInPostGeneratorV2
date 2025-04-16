from dotenv import load_dotenv

from langchain_groq import ChatGroq
import os

load_dotenv()

llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama-3.3-70b-versatile")

def generate_llm_response(filtered_posts, llm_input):
    # Logic to call the LLM (Groq API or similar)
    # Here you would use the filtered posts and the llm_input to generate a refined LinkedIn post.
    # Example (pseudo code):
    response = groq_api.generate(
        prompt=f"Generate a refined LinkedIn post using the following examples: {filtered_posts} and input: {llm_input}"
    )
    return response


if __name__== "__main__":
    # Test the LLM
    response = llm.invoke("chichen curry kaise banate hai")
    print(response.content)