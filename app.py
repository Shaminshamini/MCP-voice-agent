import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECIPIENT_PHONE_NUMBER = os.getenv("RECIPIENT_PHONE_NUMBER")

def get_voice_audio(prompt):
    url = "https://api.elevenlabs.io/v1/text-to-speech/your-voice-id"
    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": prompt,
        "voice_settings": {"stability": 0.75, "similarity_boost": 0.75}
    }
    response = requests.post(url, headers=headers, json=data)
    audio_url = response.json().get("audio_url")
    return audio_url

def make_call(audio_url):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        twiml=f'<Response><Play>{audio_url}</Play></Response>',
        to=RECIPIENT_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER
    )
    print(f"Call initiated: {call.sid}")

if __name__ == "__main__":
    with open("prompt_template.txt", "r") as file:
        prompt = file.read()
    audio_url = get_voice_audio(prompt)
    if audio_url:
        make_call(audio_url)
