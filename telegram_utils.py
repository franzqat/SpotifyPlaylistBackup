from telegram import Bot

def create_telegram_message(copied_songs):
    """Create the Telegram message with the list of copied songs."""
    message = "✅ Playlist backup successfully! 🎉\n\nHere's the list of the songs:\n\n"
    for song in copied_songs:
        message += f"- {song['artist']} - {song['name']}\n"
    return message

async def send_telegram_message(telegram_token, chat_id, message):
    """Send a message to the Telegram bot."""
    bot = Bot(token=telegram_token)
    await bot.send_message(chat_id=chat_id, text=message)
