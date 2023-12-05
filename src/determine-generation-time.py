# Estimate the time it will take to generate a given text file
# I've done very limited testing but have estimated the ElevenLabs generation speed
# To be around 16.5 characters per second
# This is heavily dependent on the length of the text, the voice model used and 11labs current server load
characters_per_second = 16.5

with open('./data/test_data.txt', 'r') as file:
    file_length = len(file.read())
    total_time_in_seconds = file_length / characters_per_second
    total_time_in_seconds = round(total_time_in_seconds, 2)
    total_time_in_minutes = total_time_in_seconds / 60
    print("File length: "+str(file_length)+" characters")
    print("Estimated generation time: " +
          str(total_time_in_minutes), "minutes")
