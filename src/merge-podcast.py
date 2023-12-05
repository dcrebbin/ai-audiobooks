from pydub import AudioSegment
import os

# Get all audio files from the chunks folder
audio_files = os.listdir(os.path.join(
    os.path.dirname(__name__), "output/chunks/"))

# Initialize combined audio file
combined = AudioSegment.empty()

# Combine all audio files
for file in audio_files:
    if file.endswith(".mp3"):
        sound = AudioSegment.from_mp3(os.path.join(
            os.path.dirname(__name__), "output/chunks/"+file))
        combined = combined + sound

# Export combined audio file
combined.export(os.path.join(
    os.path.dirname(__name__), "output/output.mp3"), format="mp3")
