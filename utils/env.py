from dotenv import load_dotenv
from os import environ

load_dotenv()

OLLAMA_HOST= environ.get("OLLAMA_HOST")