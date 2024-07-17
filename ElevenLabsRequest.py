import uuid
from elevenlabs import VoiceSettings, play
from elevenlabs.client import ElevenLabs


VoiceIDs = {
    "ALICE": "Xb7hH8MSUJpSbSDYk0k2",
}

class ElevenLabsRequest(object):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = ElevenLabs(api_key=self.api_key)

    def text_to_speech_file(self, text: str):
        try:
            response = self.client.text_to_speech.convert(
                voice_id=VoiceIDs["ALICE"],
                optimize_streaming_latency="0",
                output_format="mp3_22050_32",
                text=text,
                model_id="eleven_turbo_v2",
                voice_settings=VoiceSettings(
                    stability=0.0,
                    similarity_boost=1.0,
                    style=0.0,
                    use_speaker_boost=True,
                ),
            )

            # Play the audio (requires ffplay.exe)
            # play(response)

            # Generate unique filename and save as MP3
            save_file_path = f"{uuid.uuid4()}.mp3"
            with open(save_file_path, "wb") as f:
                for chunk in response:
                    if chunk:
                        f.write(chunk)
            
            return save_file_path
        except Exception as ex:
            print(f'Error in text_to_speech_file: {ex}')
            return None