import os
import asyncio
import logging
import spotipy_utils
import telegram_utils

# Configure logging to output to stdout
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def main():
    # Log the start of the process
    logging.info("Starting application")

    # Retrieve Spotify API credentials from environment variables
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
    redirect_uri = "http://localhost:8888/callback/"

    # Log the retrieval of environment variables
    logging.info("Retrieved environment variables")

    # Retrieve Telegram bot token and chat ID from environment variables
    telegram_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    # Source and destination playlist IDs
    source_playlist_id = os.environ.get("SPOTIFY_SOURCE_PLAYLIST")
    destination_playlist_id = os.environ.get("SPOTIFY_DEST_PLAYLIST")

    # Create a new instance of the Spotipy client with authentication
    sp = spotipy_utils.create_spotify_client(client_id, client_secret, redirect_uri)

    # Log successful Spotify client creation
    logging.info("Spotify client created successfully")

    # Get all tracks from the source playlist
    track_uris = spotipy_utils.get_playlist_tracks(sp, source_playlist_id)
    logging.info(f"Retrieved {len(track_uris)} tracks from source playlist")

    # Add the tracks to the destination playlist
    spotipy_utils.add_tracks_to_playlist(sp, destination_playlist_id, track_uris)
    logging.info(f"Added tracks to destination playlist")

    # Get the names of the copied songs
    copied_songs = spotipy_utils.get_track_names(sp, track_uris)
    logging.info("Retrieved copied songs' names")

    # Create the Telegram message
    message = telegram_utils.create_telegram_message(copied_songs)
    logging.info("Telegram message created")

    # Send the Telegram message
    await telegram_utils.send_telegram_message(telegram_token, chat_id, message)
    logging.info("Telegram message sent")

# Run the async function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
