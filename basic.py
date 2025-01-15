from typing import Any
import requests

OLLAMA_API = "http://192.168.1.195:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

messages = [
    {"role": "user", "content": "What is the capital of Nepal?"},
]

payload = {"model": MODEL, "messages": messages, "stream": False}

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
json_response: dict[str, Any] = response.json()
print(json_response.get("message", {}).get("content"))
