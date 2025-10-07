import os
from google import genai
from google.genai import types

# Set the model name using the official, up-to-date name

MODEL_NAME = 'gemini-2.5-flash' 

# Initialize the Gemini Client
# It automatically picks up the API key from the environment variable GEMINI_API_KEY
try:
    client = genai.Client()
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    print("Please ensure you have set the GEMINI_API_KEY environment variable.")
    exit()

def generate_password() -> str:
    """
    Generates a strong password using the Gemini model.
    """
    # Define the prompt (which was in the 'sem' block)
    prompt = """
    Generate a single, strong password. 
    The password must be 12 characters or longer and must include 
    at least one uppercase letter, one lowercase letter, one digit, and one symbol. 
    Do not include any other text or explanation, just the password.
    """
    
    # Configure the generation for best results (e.g., lower temperature for deterministic output)
    config = types.GenerateContentConfig(
        temperature=0.4,
    )
    
    # Call the model
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt],
        config=config,
    )
    
    # Return the clean, generated text (the password)
    return response.text.strip()

# Standard Python entry point
if __name__ == "__main__":
    # This replaces the non-standard 'with entry { print(...); }'
    try:
        password = generate_password()
        print(f"Generated Password: {password}")
    except Exception as e:
        print(f"An error occurred during password generation: {e}")