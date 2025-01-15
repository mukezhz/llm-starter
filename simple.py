import ollama
from utils.scrape import get_text_from_url

OLLAMA_HOST = "http://192.168.1.195:11434"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

title, text = get_text_from_url("https://mukesh.name.np")

def get_messages(title: str, text: str):
    messages: list[dict[str, str]] = []
    message = f"""Provide the short summary of the website.
    This is the title of website: {title}
    And this is the content of the website:
    {text}
    """
    messages.append({"role": "user", "content": message})
    return messages

ollama_client = ollama.Client(host=OLLAMA_HOST)
response = ollama_client.chat(model=MODEL, messages=get_messages(title, text), stream=False)

print(response.get("message", {}).get("content"))
