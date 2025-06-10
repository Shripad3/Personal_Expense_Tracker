import dotenv
import os
from google import generativeai as genai

def ask_gemini(prompt_text):
    dotenv.load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')

    genai.configure(api_key=os.getenv(api_key))
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt_text)
    return response.text