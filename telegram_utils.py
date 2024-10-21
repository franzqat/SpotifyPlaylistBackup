import logging
from telegram import Bot, TelegramError


def create_telegram_message(copied_songs):
    """Create the Telegram message with the list of copied songs."""
    message = "✅ Playlist backup successfully! 🎉\n\nHere's the list of the songs:\n\n"
    for song in copied_songs:
        message += f"- {song['artist']} - {song['name']}\n"
    return message


logger = logging.getLogger(__name__)


async def send_telegram_message(telegram_token, chat_id, message):
    """Send a message to the Telegram bot."""
    bot = Bot(token=telegram_token)
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        logger.info("Message sent successfully")
    except TelegramError as e:
        logger.error(f"Failed to send message: {e}")
