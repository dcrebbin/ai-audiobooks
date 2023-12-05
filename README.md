# ElevenLabs Podcaster

_Turn your text data into a full length podcast or audiobook with ElevenLabs!_

## Example

Play ```/example/intro-to-algos-asmr-lmao.mp3```

This is an extract from "Introduction to Algorithms
Fourth Edition" purchase the book from MIT here: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/

As it was just copied straight from the PDF there are a few syntax errors within the data that have resulted in strange generations.

when doing real world testing making sure to clean your data fire and do a few small test runs while modifying the voice settings within /src/generate-podcast:

```
"voice_settings": {
    "similarity_boost": 0.8,
    "stability": 0.8,
}
```

ElevenLabs API reference https://elevenlabs.io/docs/api-reference/text-to-speech

## Installation

1. pip install -r ./requirements

2. Create an ElevenLabs account and retrieve an API key

3. Create a **.env** file and add you API key (using env.example as a template)

4. Copy and paste the text you want to turn into a podcast and put it in ./data/test_data.txt

5. Run `python ./src/determine-cost.py` to work out how much it would cost to create

5. Run `python ./src/determine-generation-time.py` to find out an estimate time it will take to generate

6. Run `python ./src/generate-podcast.py`

   _Note: Running the generation script will chunk up the files and process each of them in order to mitigate any overly long API requests that become more volatile over their run time_

7. Run `python ./src/merge-podcast.py` to merge all audio files within ./output/chunks into a single file named **output.mp3**

8. Enjoy!

For more open source hacky projects: visit [my github :)](https://github.com/dcrebbin)
