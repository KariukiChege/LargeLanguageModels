import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

ollama_api_key = os.getenv("OLLAMA_API_KEY")
OLLAMA_BASE_URL = "http://localhost:11434/v1"
check_connection = requests.get(OLLAMA_BASE_URL + "/models").content
#print(check_connection)

client = OpenAI(base_url=OLLAMA_BASE_URL, api_key=ollama_api_key)
response = client.chat.completions.create(
    model="llama3.2:latest",  
    messages=[{'role': 'user', 'content': 'Reply with exactly: Hola Mundo!'}]
)
print(response.choices[0].message.content)