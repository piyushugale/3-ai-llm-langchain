import os
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI  # correct import for LangChain's Google GenAI

# Ensure API key is set
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Send prompt and store the response
response = model.invoke("Hello, world!")

# Print the result
print(response.content)  # .content gives you the actual text


'''
$ python 3-llm-chatmodel.py

Output:
Enter API key for Google Gemini: ***********

Hello, world indeed! A classic.
How can I help you today?

'''