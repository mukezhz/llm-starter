from dotenv import load_dotenv
from os import environ

load_dotenv()

OLLAMA_HOST= environ.get("OLLAMA_HOST")
OPENAI_API_KEY= environ.get("OPENAI_API_KEY")
OPENAI_BASE_URL= environ.get("OPENAI_BASE_URL")