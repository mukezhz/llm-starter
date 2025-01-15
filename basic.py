from typing import Any
import requests

from utils.env import OLLAMA_HOST

HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"


messages = [
    {"role": "user", "content": "What is the capital of Nepal?"},
]

payload = {"model": MODEL, "messages": messages, "stream": False}

url = f"{OLLAMA_HOST}/api/chat"
response = requests.post(url=url, json=payload, headers=HEADERS)
json_response: dict[str, Any] = response.json()
print(json_response.get("message", {}).get("content"))
