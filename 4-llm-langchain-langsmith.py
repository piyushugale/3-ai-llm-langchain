'''
Build a simple LLM application with chat models and prompt templates
Reference: https://python.langchain.com/docs/tutorials/llm_chain/
LangSmith: Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. 
           As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. 
           The best way to do this is with LangSmith.
1. Using language models
2. Using prompt templates
3. Debugging and tracing your application using LangSmith
'''
# pip install langchain


'''
LangSmith
Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with LangSmith.

After you sign up at the link above, make sure to set your environment variables to start logging traces:

    export LANGSMITH_TRACING="true"
    export LANGSMITH_API_KEY="..."
    export LANGSMITH_PROJECT="default" 

Powershell:
    $env:LANGSMITH_TRACING="true"
    $env:LANGSMITH_API_KEY="..."
    $env:LANGSMITH_PROJECT="default" 
'''

# Using Language Models

import os
import getpass
from langchain_core.messages import HumanMessage, SystemMessage

# Ensure API key is set
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# To simply call the model, we can pass in a list of messages to the .invoke method.
# HumanMessage | SystemMessage

messages = [
    SystemMessage("Translate the following from English into Italian:"),
    HumanMessage("hi, how are you?!"),
]

# response = model.invoke(messages)
# print(response.content)

# model.invoke("Hello")
# model.invoke([{"role": "user", "content": "Hello"}])
# model.invoke([HumanMessage("Hello")])


'''
Output:

Enter API key for Google Gemini: 
**नमस्कार, आज तुम्ही कसे आहात?!**

*   **नमस्कार** (Namaskar) - Hello
*   **आज** (Aaj) - today
*   **तुम्ही कसे आहात** (Tumhi kase aahat) - how are you (formal/plural 'you')
*   **?!** - (exclamation and question marks, as in English)

You could also say:

*   **हॅलो, आज तुम्ही कसे आहात?!** (Hॅlo, aaj tumhi kase aahat?!) - using the transliterated "Hello"
*   **नमस्कार, आज काय चाललंय?** (Namaskar, aaj kaay chaallay?) - More informal, like "Hello, what's up today?" or "Hello, how's it going today?"
'''

# Streaming
# Because chat models are Runnables, they expose a standard interface that includes async and streaming modes of invocation. This allows us to stream individual tokens from a chat model:

for token in model.stream(messages):
    print(token.content, end="|")

