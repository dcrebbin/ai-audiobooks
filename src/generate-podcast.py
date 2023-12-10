import os
import requests
import re
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
    # Open text file with UTF-8 encoding
    with open('./data/test_data.txt', 'r', encoding='utf-8') as file:
        # Use regular expression to keep periods with sentences
        text_array = re.split(r'(?<=\.)\s+', file.read().strip())

        # Check if there is an uneven number of sentences
        if len(text_array) % 2 != 0:
            # Add an empty string to make it even
            text_array.append("")

        sentences_to_process = list(zip(text_array[0::2], text_array[1::2]))

        # Iterate sentence pairs and generate audio for each pair
        for index, (first_sentence, second_sentence) in enumerate(sentences_to_process):
            combined_sentence = first_sentence
            combined_sentence += ' ' + second_sentence if second_sentence else ''
            await generate_voice(combined_sentence, index)
            print(combined_sentence)
    print("Finished generation! Don't forget to run python ./src/merge-podcast.py to combine all audio files 🤠")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
