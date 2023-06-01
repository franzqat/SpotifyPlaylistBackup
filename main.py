import os
import asyncio
# from spotipy.oauth2 import SpotifyOAuth
import spotipy_utils
import telegram_utils

async def main():
    # Retrieve Spotify API credentials from environment variables
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
    redirect_uri = "http://localhost:8888/callback/"

    # Retrieve Telegram bot token and chat ID from environment variables
    telegram_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id =  os.environ.get("TELEGRAM_CHAT_ID")

    # Source and destination playlist IDs
    source_playlist_id = os.environ.get("SPOTIFY_SOURCE_PLAYLIST")
    destination_playlist_id = os.environ.get("SPOTIFY_DEST_PLAYLIST")

    # Create a new instance of the Spotipy client with authentication
    sp = spotipy_utils.create_spotify_client(client_id, client_secret, redirect_uri)

    # Get all tracks from the source playlist
    track_uris = spotipy_utils.get_playlist_tracks(sp, source_playlist_id)

    # Add the tracks to the destination playlist
    spotipy_utils.add_tracks_to_playlist(sp, destination_playlist_id, track_uris)

    # Get the names of the copied songs
    copied_songs = spotipy_utils.get_track_names(sp, track_uris)

    # Create the Telegram message
    message = telegram_utils.create_telegram_message(copied_songs)

    # Send the Telegram message
    await telegram_utils.send_telegram_message(telegram_token, chat_id, message)

# Run the async function
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
