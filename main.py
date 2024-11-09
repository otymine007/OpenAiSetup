import openai
from config.config import get_openai_api_key

# Set the OpenAI API key
openai.api_key = get_openai_api_key()

# Example: Send a prompt to the GPT model using the new chat API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # You can use other models like "gpt-4"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello to the world!"}
    ]
)

print(response['choices'][0]['message']['content'])