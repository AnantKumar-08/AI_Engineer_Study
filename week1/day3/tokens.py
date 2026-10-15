import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("No api key found")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"

#3 prompts
prompt1="Hii!"
prompt2="Explain time travel in details in 100 words"
prompt3="write a essay of 1000 words on machine learning"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message={
    "role":role,
    "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=50)
    usage=response.usage
    print(f"Prompt: {prompt} --> Your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} Total_tokens: {usage.prompt_tokens+usage.completion_tokens}, Finish_reason: {response.choices[0].finish_reason}")

# # prompt="Do you know carryminati"

# messages = [message]

# response = client.chat.completions.create(model=model, messages=messages)
# print(response)

# print("###################################################")

# answer=response.choices[0].message.content
# print(answer)