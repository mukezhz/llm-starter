from openai import OpenAI

from utils.env import OPENAI_API_KEY, OPENAI_BASE_URL

client = OpenAI(
    # This is the default and can be omitted
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the capital of the United States?",
        }
    ],
    model="gpt-3.5-turbo",
)
for choice in chat_completion.choices:
    print(choice.message.content)