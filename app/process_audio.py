import asyncio
import subprocess
import os
from fast_whisper import fast_transcribe

async def process_voice(path: str) -> str:
    wav_path = f"{path}.wav"

    command = [
        "ffmpeg", "-y",
        "-i", path,
        "-ar", "16000",
        "-ac", "1",
        "-loglevel", "error",
        wav_path
    ]

    # Run ffmpeg without blocking the event loop
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, lambda: subprocess.run(command, check=True))

    # Transcribe
    text = await fast_transcribe(wav_path)

    # Clean files
    os.remove(wav_path)
    os.remove(path)

    return text
