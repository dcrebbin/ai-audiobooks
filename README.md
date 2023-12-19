# AI Audiobookster

_Turn your text data into a full length podcast or audiobook with AI!_

Supports:
- ElevenLabs
- OpenAI
- Unreal Speech

## Example

Play `/example/eleven_labs_intro-to-algos-asmr-lmao.mp3`

This is an extract from "Introduction to Algorithms
Fourth Edition" purchase the book from MIT here: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

As it was just copied straight from the PDF there are a few syntax errors within the data that have resulted in strange generations.

when doing real world testing making sure to clean your data fire and do a few small test runs while modifying the voice settings within your given AI providers settings located in ./src/ai_provider_settings

### ElevenLabs

ElevenLabs API reference https://elevenlabs.io/docs/api-reference/text-to-speech

### OpenAi

OpenAI API reference https://platform.openai.com/docs/api-reference/audio/createSpeech

### Unreal Speech

Unreal Speech API reference https://docs.unrealspeech.com/#b555f89b-526e-4212-97d3-6c9687bb2219

## Installation

1. pip install -r ./requirements

2. Create an ElevenLabs/OpenAi/Unreal Speech account and retrieve an API key

3. Create a **.env** file and add your API key (using env.example as a template)

4. Copy and paste the text you want to turn into a podcast and put it in ./data/test_data.txt

5. Run `python ./src/determine-cost.py elevenlabs|openai|unrealspeech` to work out how much it would cost to create dependent on the AI provider you're using

6. Run `python ./src/determine-generation-time.py elevenlabs|openai|unrealspeech` to find out an estimate time it will take to generate

7. Run `python ./src/generate-podcast.py elevenlabs|openai|unrealspeech`

   _Note: Running the generation script will chunk up the files and process each of them in order to mitigate any overly long API requests that become more volatile over their run time_

8. Run `python ./src/merge-podcast.py` to merge all audio files within ./output/chunks into a single file named **output.mp3**

9. Enjoy!

For more open source hacky projects: visit [my github :)](https://github.com/dcrebbin)
