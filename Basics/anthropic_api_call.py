import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = OpenAI()

response = client.chat.completions.create(
    model="claude-sonnet-5", 
    messages=[{'role': 'user', 'content': 'Reply with exactly: Habari Dunia!'}]
)

print(response.choices[0].message.content)
