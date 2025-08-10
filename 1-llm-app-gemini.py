# LangChain: https://python.langchain.com/docs/introduction/

import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env into environment
load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="add 20 dashes. Explain how AI works in a one liner. add 20 dashes"
)
print(response.text)
