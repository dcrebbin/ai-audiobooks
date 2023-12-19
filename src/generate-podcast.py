import requests
import re
import sys
import ai_provider_settings

# Load environment variables from .env file

# File extension for generated audio
EXTENSION = ".mp3"

try:
    # Get AI argument from command line
    # Specify which AI to use to generate the audio: elevenlabs/openai/unrealspeech
    SELECTED_AI_ARGUMENT = sys.argv[1]
except IndexError:
    print("Please provide an AI argument")
    print(
        "Usage: python3 src/determine-cost.py [elevenlabs/openai/unrealspeech]")
    sys.exit()

# Generic request headers
headers = {
    "Content-Type": "application/json",
    "Accept": "audio/mp3",
}

# Function for generating audio from text
async def generate_voice(text, index):
    print(f"Generating voice for: {index}")

    # Get the AI provider specific generation endpoint and payload
    API_URL = ai_provider_settings.get_url(SELECTED_AI_ARGUMENT)
    PAYLOAD = ai_provider_settings.get_payload(SELECTED_AI_ARGUMENT, text)

    # Update header with AI provider specific authentication
    auth_header = ai_provider_settings.get_auth(SELECTED_AI_ARGUMENT)
    headers[auth_header["type"]] = auth_header["value"]

    print(f"Sending request to: {API_URL}")
    response = requests.post(API_URL, json=PAYLOAD, headers=headers)
    
    # Check for errors
    success = False
    while not success:
        # Make API request
        response = requests.post(API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            print(f"Writing audio file for index: {index}")

            # Write audio content to file
            with open(f'./output/chunks/test_data{index}{EXTENSION}', 'wb') as file:
                file.write(response.content)
            success = True
        else:
            print(f"Error: {response.text}. Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying

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
