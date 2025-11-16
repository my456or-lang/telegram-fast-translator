import asyncio
import subprocess
import os
from fast_whisper import fast_transcribe

async def process_voice(path):
    wav_path = path + ".wav"

    # Convert to WAV quickly
    command = ["ffmpeg", "-y", "-i", path, "-ar", "16000", "-ac", "1", wav_path]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    text = await fast_transcribe(wav_path)

    os.remove(wav_path)
    return text
