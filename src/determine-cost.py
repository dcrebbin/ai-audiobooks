import sys;

ELEVEN_LABS_COST_PER_1000_CHARACTERS = 0.3
# Cost per 1000 characters only applies when your ElevenLabs account has exceeded your current tier
# For more information on ElevenLabs up to date pricing visit: https://elevenlabs.io/subscription
# Currently 30c (0.3 USD) per 1000 characters

OPEN_AI_COST_PER_1000_CHARACTERS = 0.015
# Cost per 1000 characters is applied to all requests to OpenAI's API
# For more information on ElevenLabs up to date pricing visit: https://elevenlabs.io/subscription
# Currently 0.015 USD per 1000 characters

UNREAL_SPEECH_COST_PER_1000_CHARACTERS = 0.01
# Cost per 1000 characters is a broad estimation based on UnrealSpeech's pricing page
# For more information on ElevenLabs up to date pricing visit: https://unrealspeech.com/pricing
# Currently 0.01 USD per 1000 characters

try:
    # Get AI argument from command line
    # Specify which AI to use when determining cost: elevenlabs/openai/unrealspeech
    SELECTED_AI_ARGUMENT = sys.argv[1]
except IndexError:
    print("Please provide an AI argument")
    print("Usage: python3 src/determine-cost.py [elevenlabs/openai/unrealspeech]")
    sys.exit()

def determine_cost_based_on_ai():
    switch = {
        "elevenlabs": ELEVEN_LABS_COST_PER_1000_CHARACTERS,
        "openai": OPEN_AI_COST_PER_1000_CHARACTERS,
        "unrealspeech": UNREAL_SPEECH_COST_PER_1000_CHARACTERS,
    }
    return switch.get(SELECTED_AI_ARGUMENT, "Invalid AI argument")

cost_by_character = determine_cost_based_on_ai() / 1000
 
# Estimate the cost of generating a given text file
with open('./data/test_data.txt', 'r') as file:
    file_length = len(file.read())
    total_cost = file_length * cost_by_character
    total_cost = round(total_cost, 4)
    print("File length: "+str(file_length)+" characters")
    print("Total cost: $"+str(total_cost)+" USD")