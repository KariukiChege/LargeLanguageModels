import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI()

response = openai_client.chat.completions.create(
    model='gpt-4.1-mini', 
    messages=[{"role": "user", "content": "Reply with exactly: Hello World!"}])


print(response.choices[0].message.content)