import ollama
from utils.env import OLLAMA_HOST
from utils.scrape import get_text_from_url

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


host = OLLAMA_HOST or "http://localhost:11434"
ollama_client = ollama.Client(host=host)
response = ollama_client.chat(
    model=MODEL, messages=get_messages(title, text), stream=False
)

print(response.get("message", {}).get("content"))
