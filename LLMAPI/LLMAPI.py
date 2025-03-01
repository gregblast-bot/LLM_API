import google.generativeai as genai
import os

api_file = open("GeminiAPIKey/APIKey.txt", "r")
key = api_file.readline()
genai.configure(api_key = key)  # get's your key

model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # replace with your model

prompt_parts = [
  "Give me a riddle with four multiple choice answers where only one is right"  # text prompt (can be before, after, or interleaved)
]

response = model.generate_content(prompt_parts)  # the actual call
print(response.text)