# Cost per 1000 characters only applies when your ElevenLabs account has exceeded your current tier
# For more information on ElevenLabs up to date pricing visit: https://elevenlabs.io/subscription
# Currently 30c (0.3 USD) per 1000 characters
cost_by_character = 0.3/1000

with open('./data/test_data.txt', 'r') as file:
    file_length = len(file.read())
    total_cost = file_length * cost_by_character
    total_cost = round(total_cost, 4)
    print("File length: "+str(file_length)+" characters")
    print("Total cost: $"+str(total_cost)+" USD")
