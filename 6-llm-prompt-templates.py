'''
Prompt templates are a concept in LangChain designed to assist with this transformation. 
They take in raw user input and return data (a prompt) that is ready to pass into a language model.

Let's create a prompt template here. It will take in two user variables:
 - language: The language to translate text into
 - text: The text to translate
'''
import os
import getpass
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

# Generate prompt text
prompt_text = prompt_template.invoke({"language": "Italian", "text": "hi!"})
print(prompt_text)
prompt_text.to_messages()

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

response = model.invoke(prompt_text)
print(response.content)

'''
Output:

Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
messages=[SystemMessage(content='Translate the following from English into Italian', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi!', additional_kwargs={}, response_metadata={})]
Ciao!

'''