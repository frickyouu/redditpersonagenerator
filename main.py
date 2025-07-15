__version__ = "1.0"

# main.py

import os
import re
import argparse
from dotenv import load_dotenv
import google.generativeai as genai

# Import your functions from the other files
from scraper import scrape_redditor_data
from llm import generate_persona

def get_username_from_url(url: str):
    match = re.search(r'user/([^/]+)', url)
    if match:
        return match.group(1)
    return None

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description="Generate a Reddit user persona.")
    parser.add_argument("url", help="The URL of the Reddit user's profile.")
    args = parser.parse_args()

    username = get_username_from_url(args.url)
    if not username:
        print("Error: Could not extract a valid username from the URL.")
        return

    # Call the imported scraper function
    scraped_data = scrape_redditor_data(username)

    if not scraped_data:
        print(f"No data found for user '{username}'. Cannot generate a persona.")
        return

    # Call the imported LLM function
    persona = generate_persona(scraped_data, username)

    # Save the output
    output_filename = f"{username}_persona.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(persona)
    
    print(f"Persona successfully saved to {output_filename}")

if __name__ == "__main__":
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    main()