'''
 The "thinking" feature enabled by default to enhance response quality. 
 You should be aware that this may increase response time and token usage. 
 If you prioritize speed or wish to minimize costs, you can disable this feature by setting the thinking budget to zero, as shown in the examples below. 
'''

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a 3 lines. All 3 lines shoulbd be printed in next lines",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)

print(response.text)