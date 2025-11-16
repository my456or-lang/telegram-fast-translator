import asyncio
from faster_whisper import WhisperModel

# Load model ONCE (fast!)
model = WhisperModel("medium", device="cpu", compute_type="int8")

async def fast_transcribe(path: str) -> str:
    loop = asyncio.get_event_loop()
    segments, _ = await loop.run_in_executor(None, lambda: model.transcribe(path))

    return " ".join([s.text for s in segments])
