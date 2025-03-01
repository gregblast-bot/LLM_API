import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])  # get's your key

model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # replace with your model

prompt_parts = [
  "Describe a flower"  # text prompt (can be before, after, or interleaved)
]

response = model.generate_content(prompt_parts)  # the actual call
print(response.text)