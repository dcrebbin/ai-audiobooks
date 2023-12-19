import sys
# Estimate the time it will take to generate a given text file
# This is heavily dependent on the length of the text, the voice model used, other specific settings and AI provider's current server load
# These values are based on the average time it took to generate the test_data.txt file using each AI provider (with minimal testing)
# These values are not guaranteed to be accurate, but are a good guideline for estimating generation time
ELEVEN_LABS_CHARACTERS_PER_SECOND = 16.5
OPEN_AI_CHARACTERS_PER_SECOND = 62.5
UNREAL_SPEECH_CHARACTERS_PER_SECOND = 86.5

try:
    # Get AI argument from command line
    # Specify which AI to use when determining cost: elevenlabs/openai/unrealspeech
    SELECTED_AI_ARGUMENT = sys.argv[1]
except IndexError:
    print("Please provide an AI argument")
    print(
        "Usage: python3 src/determine-cost.py [elevenlabs/openai/unrealspeech]")
    sys.exit()


def determine_characters_per_second_based_on_ai():
    switch = {
        "elevenlabs": ELEVEN_LABS_CHARACTERS_PER_SECOND,
        "openai": OPEN_AI_CHARACTERS_PER_SECOND,
        "unrealspeech": UNREAL_SPEECH_CHARACTERS_PER_SECOND,
    }
    return switch.get(SELECTED_AI_ARGUMENT, "Invalid AI argument")

characters_per_second = determine_characters_per_second_based_on_ai()

with open('./data/test_data.txt', 'r') as file:
    file_length = len(file.read())
    total_time_in_seconds = file_length / characters_per_second
    total_time_in_seconds = round(total_time_in_seconds, 2)
    total_time_in_minutes = total_time_in_seconds / 60
    print("File length: "+str(file_length)+" characters")
    print("Estimated generation time: " +
          str(total_time_in_minutes), "minutes")
