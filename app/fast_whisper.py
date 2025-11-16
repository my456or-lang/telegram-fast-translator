import asyncio
from faster_whisper import WhisperModel

# Load a fast model (medium recommended for speed/quality balance)
model = WhisperModel("medium", device="cpu", compute_type="int8")

async def fast_transcribe(path):
    segments, _ = model.transcribe(path)
    return " ".join([s.text for s in segments])
