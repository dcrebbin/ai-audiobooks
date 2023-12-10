import os
import subprocess

# Directory containing the MP3 files
directory = './output/chunks/'

# Check if filelist.txt exists and clear it
filelist_path = os.path.join(directory, 'filelist.txt')
if os.path.exists(filelist_path):
    os.remove(filelist_path)

# Fetch all mp3 files and sort them numerically
files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# Write the sorted file names to filelist.txt
with open(filelist_path, 'w') as file:
    for f in files:
        file.write(f"file '{f}'\n")

# Run FFmpeg command
output_file = os.path.join('./output/', 'output.mp3')
ffmpeg_command = f'ffmpeg -f concat -safe 0 -i "{filelist_path}" -c copy "{output_file}"'
subprocess.run(ffmpeg_command)

