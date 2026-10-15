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

#Structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
    phoneNo: int

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the information from the ticket strictly based on this schema and give me json output and also give me issue in as shortest form as possible 
{schema}
"""
message_system={
    "role": "system",
    "content": system_prompt
}

text="Hello my name is Anant. I have purchased an iPhone from your store and it stopped working. And i also broke up with my girlfrined, My height is 5'10. My email is abc@gmail.com. and my contact number is 34543. Baki ke information se tu kya le etne me he kaam chla na"
prompt=f"""
This is a customer ticket. Please extract the personal information from this,
{text}
"""
message={
    "role":role,
    "content": prompt
}
messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)

# isko padhte kese hai?
import json
raw_json= answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)