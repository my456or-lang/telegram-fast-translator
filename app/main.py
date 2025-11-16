import asyncio
import os
from telegram.ext import Application, MessageHandler, filters
from process_audio import process_voice

TOKEN = os.getenv("BOT_TOKEN")  # from Render ENV

async def handle_voice(update, context):
    file = await update.message.voice.get_file()
    file_path = await file.download_to_drive()

    text = await process_voice(file_path)
    await update.message.reply_text(text)

def run():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    application.run_polling()

if __name__ == "__main__":
    run()
