import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents
from rich.console import Console
from rich.markdown import Markdown
# from IPython.display import Markdown, display

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

website_url = fetch_website_contents("https://www.infoworld.com/article/4204585/when-the-cloud-control-plane-fails.html")

system_prompt = "You are a helpful assistant. Your task is to summarize the contents of an article written by David Linthicum" \
"You only concentrate on the text of the article in the website and you ignore all other content or links that are not part of the" \
"article. Do not wrap the markdown in a code block - respond in markdown format only."

user_prompt = f"Summarize the following article by David Linthicum:\n\n{website_url} in markdown format. If it includes news or" \
"announcements, that are not part of the article. ignore them."

def process_prompt():
    return [
        {"role": "system", "content": system_prompt },
        {"role": "user", "content": user_prompt }
    ]

def summarize_article():
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=process_prompt()
    )
    return response.choices[0].message.content

console = Console()

def display_summary():
    summary = summarize_article()
    # Depending on your IDE the console type of markdown or the display type of markdown
    console.print(Markdown(f'DAVID LINTHICUM SUMMARY:\n\n{summary}'))

    # display(Markdown(summary))

display_summary()
