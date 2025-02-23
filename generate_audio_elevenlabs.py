import requests
import os

API_KEY = os.getenv("ELEVEN_LABS_API_KEY")  # api key from elevenlabs
VOICE_ID = "MF3mGyEYCl7XYWbV9V6O"  # Standard Indian-accented voice

script_text = """Namaste Mathangi! My name is Anika, and I’m here to guide you through managing your credit 
card dues. Mathangi, as of today, your credit card bill shows an amount due of INR 5,053 which 
needs to be paid by 31st December 2024. Missing this payment could lead to two significant consequences: 
First, a late fee will be added to your outstanding balance. Second, your credit score will be negatively impacted, 
which may affect your future borrowing ability. Make your payment by clicking the link here... 
Pay through UPI or bank transfer. Thank you!"""

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {"xi-api-key": API_KEY}
data = {"text": script_text, "model_id": "eleven_monolingual_v1", "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}}

response = requests.post(url, json=data, headers=headers)

# audio file
if response.status_code == 200:
    with open("audio.mp3", "wb") as f:
        f.write(response.content)
    print("Audio generated successfully! Check audio.mp4")
else:
    print("Error:", response.json())
