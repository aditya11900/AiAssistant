import os
import openai
from config import apikey

openai.api_key = "Apikey"

response = openai.Completion.create(
  model="gpt-3.5-turbo-0125",
  prompt=" ",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)