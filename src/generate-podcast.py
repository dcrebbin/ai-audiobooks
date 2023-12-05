import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API and Audio Settings
# Model ID for Elevenlabs text-to-speech API
MODEL_ID = "eleven_multilingual_v2"

# File extension for generated audio
EXTENSION = ".mp3"

# Voice ID for the "ASMR" voice
VOICE_ID = "piTKgcLEGmPE4e6mEKli"

# API endpoint with voice ID
API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

# Request Headers
# Includes API key from environment variables
# And sets content type to JSON
headers = {
    "Content-Type": "application/json",
    "xi-api-key": os.getenv("ELEVEN_API_KEY")
}

# Function to generate audio from text

async def generate_voice(text, index):
    """
    Uses the Elevenlabs API to generate audio file from input text

    Parameters:
        text (str): The text to convert to speech
        index (int): The index value for naming output file

    Returns:
        None 
    """

    print(f"Generating voice for: {index}")

    # API payload with text, voice model and settings
    payload = {
        "model_id": MODEL_ID,
        "text": text,
        "voice_settings": {
            "similarity_boost": 0.95,
            "stability": 0.85
        }
    }

    # Make API request
    response = requests.post(API_URL, json=payload, headers=headers)

    # Check for errors
    if response.status_code != 200:
        print(f"Error: {response.text}")

    else:
        print(f"Writing audio file for index: {index}")

        # Write audio content to file
        with open(f'./output/chunks/test_data{index}{EXTENSION}', 'wb') as file:
            file.write(response.content)

# Main function

async def main():
    # Open text file and split into sentences
    with open('./data/test_data.txt', 'r') as file:
        text_array = file.read().split(".")

        # Iterate sentences and generate audio for each
        for index, text in enumerate(text_array):
            await generate_voice(text, index)
            print(text)
    print("Finished generation! Don't forget to run python ./src/merge-podcast.py to combine all audio files 🤠")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
