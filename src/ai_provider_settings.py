import os
from dotenv import load_dotenv
load_dotenv()

# Model ID for the latest Elevenlabs text-to-speech API
ELEVEN_LABS_MODEL_ID = "eleven_multilingual_v2"
# Voice ID for the "ASMR" voice
ELEVEN_LABS_VOICE_ID = "piTKgcLEGmPE4e6mEKli"
ELEVEN_LABS_ENDPOINT = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_LABS_VOICE_ID}"

OPEN_AI_MODEL_ID = "tts-1"
# Generic voice ID for OpenAI's API
OPEN_AI_VOICE_ID = "alloy"
OPEN_AI_ENDPOINT = "https://api.openai.com/v1/audio/speech"

# Generic voice ID for Unreal Speech's API
UNREAL_SPEECH_VOICE_ID = "Liv"
UNREAL_SPEECH_ENDPOINT = "https://api.v6.unrealspeech.com/stream"

AI_PROVIDER_SETTINGS = {
    "elevenlabs": {
        "url": ELEVEN_LABS_ENDPOINT,
        "auth_type": "xi-api-key",
        "auth_value": os.getenv("ELEVEN_LABS_API_KEY",""),
        "text_input_name": "text",
        "payload": {
            "model_id": ELEVEN_LABS_MODEL_ID,
            "text": "",
            "voice_settings": {
                "similarity_boost": 0.95,
                "stability": 0.85
            }
        }
    },
    "openai": {
        "url": OPEN_AI_ENDPOINT,
        "auth_type": "Authorization",
        "auth_value": "Bearer " + os.getenv("OPEN_AI_API_KEY",""),
        "text_input_name": "input",
        "payload": {
            "model": OPEN_AI_MODEL_ID,
            "input": "",
            "voice": OPEN_AI_VOICE_ID,
        }
    },
    "unrealspeech": {
        "url": UNREAL_SPEECH_ENDPOINT,
        "auth_type": "Authorization",
        "auth_value": "Bearer " + os.getenv("UNREAL_SPEECH_API_KEY",""),
        "text_input_name": "Text",
        "payload": {
            #  This payload isn't a bug, it uses title case for the property names and the ints are strings
            "Text":   "",
            "VoiceId": "Liv",
            "Bitrate": "64k",
            "Speed":   "0",
            "Pitch":   "1",
            "Codec":   "libmp3lame",
        }
    }
}

def get_payload(ai_provider, text):
    ai_config = AI_PROVIDER_SETTINGS.get(ai_provider)
    payload = ai_config.get("payload")
    payload[ai_config.get("text_input_name")] = text
    return payload

def get_auth(ai_provider):
    ai_config = AI_PROVIDER_SETTINGS.get(ai_provider)
    return {"type": ai_config.get("auth_type"), "value": ai_config.get("auth_value")}

def get_url(ai_provider):
    ai_config = AI_PROVIDER_SETTINGS.get(ai_provider)
    return ai_config.get("url")
