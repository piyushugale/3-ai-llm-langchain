#===============
# Sync streaming
#===============

from langchain_anthropic.chat_models import ChatAnthropic

chat = ChatAnthropic(model="claude-3-haiku-20240307")
for chunk in chat.stream("Write me a 1 verse song about goldfish on the moon"):
    print(chunk.content, end="|", flush=True)
    
'''
Here| is| a| |1| |verse| song| about| gol|dfish| on| the| moon|:|

Floating| up| in| the| star|ry| night|,|
Fins| a|-|gl|im|mer| in| the| pale| moon|light|.|
Gol|dfish| swimming|,| peaceful| an|d free|,|
Se|ren|ely| |drif|ting| across| the| lunar| sea|.|
'''    

#================
# Async Streaming
#================

from langchain_anthropic.chat_models import ChatAnthropic

chat = ChatAnthropic(model="claude-3-haiku-20240307")
async for chunk in chat.astream("Write me a 1 verse song about goldfish on the moon"):
    print(chunk.content, end="|", flush=True)
    
    
'''
Here| is| a| |1| |verse| song| about| gol|dfish| on| the| moon|:|

Floating| up| above| the| Earth|,|
Gol|dfish| swim| in| alien| m|irth|.|
In| their| bowl| of| lunar| dust|,|
Gl|it|tering| scales| reflect| the| trust|
Of| swimming| free| in| this| new| worl|d,|
Where| their| aqu|atic| dream|'s| unf|ur|le|d.|
'''    

#===============
# Astream events
#===============

# This method is useful if you're streaming output from a larger LLM application that contains multiple steps (e.g., an LLM chain composed of a prompt, llm and parser).

from langchain_anthropic.chat_models import ChatAnthropic

chat = ChatAnthropic(model="claude-3-haiku-20240307")
idx = 0

async for event in chat.astream_events(
    "Write me a 1 verse song about goldfish on the moon"
):
    idx += 1
    if idx >= 5:  # Truncate the output
        print("...Truncated")
        break
    print(event)
    
'''
{'event': 'on_chat_model_start', 'data': {'input': 'Write me a 1 verse song about goldfish on the moon'}, 'name': 'ChatAnthropic', 'tags': [], 'run_id': '1d430164-52b1-4d00-8c00-b16460f7737e', 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-haiku-20240307', 'ls_model_type': 'chat', 'ls_temperature': None, 'ls_max_tokens': 1024}, 'parent_ids': []}
{'event': 'on_chat_model_stream', 'run_id': '1d430164-52b1-4d00-8c00-b16460f7737e', 'name': 'ChatAnthropic', 'tags': [], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-haiku-20240307', 'ls_model_type': 'chat', 'ls_temperature': None, 'ls_max_tokens': 1024}, 'data': {'chunk': AIMessageChunk(content='', additional_kwargs={}, response_metadata={}, id='run-1d430164-52b1-4d00-8c00-b16460f7737e', usage_metadata={'input_tokens': 21, 'output_tokens': 2, 'total_tokens': 23, 'input_token_details': {'cache_creation': 0, 'cache_read': 0}})}, 'parent_ids': []}
{'event': 'on_chat_model_stream', 'run_id': '1d430164-52b1-4d00-8c00-b16460f7737e', 'name': 'ChatAnthropic', 'tags': [], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-haiku-20240307', 'ls_model_type': 'chat', 'ls_temperature': None, 'ls_max_tokens': 1024}, 'data': {'chunk': AIMessageChunk(content="Here's", additional_kwargs={}, response_metadata={}, id='run-1d430164-52b1-4d00-8c00-b16460f7737e')}, 'parent_ids': []}
{'event': 'on_chat_model_stream', 'run_id': '1d430164-52b1-4d00-8c00-b16460f7737e', 'name': 'ChatAnthropic', 'tags': [], 'metadata': {'ls_provider': 'anthropic', 'ls_model_name': 'claude-3-haiku-20240307', 'ls_model_type': 'chat', 'ls_temperature': None, 'ls_max_tokens': 1024}, 'data': {'chunk': AIMessageChunk(content=' a short one-verse song', additional_kwargs={}, response_metadata={}, id='run-1d430164-52b1-4d00-8c00-b16460f7737e')}, 'parent_ids': []}
...Truncated
''' 