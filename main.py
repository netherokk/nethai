import os
from dotenv import load_dotenv
from OpenAIRequest import OpenAIRequest
from ElevenLabsRequest import ElevenLabsRequest


load_dotenv()

openAI = OpenAIRequest(os.getenv("OA_API_KEY"))
elevenLabs = ElevenLabsRequest(os.getenv("EL_API_KEY"))

message = input("Message: ")
if message:
    response = openAI.send_message(message)
    if response:
        content = response["content"].strip()
        print(f"Response: {content}")
        save_file = elevenLabs.text_to_speech_file(response["content"])
        print(f"Audio File: {save_file}")
