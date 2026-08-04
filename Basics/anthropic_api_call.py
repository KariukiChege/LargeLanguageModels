import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1"

client = OpenAI(base_url=ANTHROPIC_BASE_URL, api_key=anthropic_api_key)

response = client.chat.completions.create(
    model="claude-sonnet-4-20250514", 
    messages=[{'role': 'user', 'content': 'Reply with exactly: Habari Dunia!'}]
)

print(response.choices[0].message.content)
