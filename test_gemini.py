import os
import google.generativeai as genai
from dotenv import load_dotenv

print("Attempting to connect to Google Gemini API...")

try:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Send a simple test prompt
    response = model.generate_content("Give me a one-sentence fun fact about computers.")
    
    print("Connection Successful!")
    print(f"Response: {response.text.strip()}")

except Exception as e:
    print(f" Connection failed. Error: {e}")
    print("Please double-check your API key and ensure it's correct in the .env file.")