import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import display, Markdown

load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai"

prompt = 'Hello, Gemini! Can you tell me a joke?'

# 1. If you have one dictionary then you don't have to use a list
message = {"role": "user", "content": prompt}

openai = OpenAI(base_url=GEMINI_BASE_URL, api_key=api_key)

response = openai.chat.completions.create(
    model="gemini-3.5-flash",
    # 2. But make sure you use a list here
    messages=[message]
)

response_text = response.choices[0].message.content
print(response_text)
