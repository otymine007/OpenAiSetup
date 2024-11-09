import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_openai_api_key():
    # Return the OpenAI API key from environment variables
    return os.getenv('OPENAI_API_KEY') 
