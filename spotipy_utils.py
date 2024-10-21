import logging
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_spotify_client(client_id, client_secret, redirect_uri):
    """Create a new instance of the Spotipy client with authentication."""
    try:
        client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="playlist-modify-private")
        )
        logger.info("Spotify client created successfully")
        return client
    except SpotifyException as e:
        logger.error(f"Failed to create Spotify client: {e}")


def get_playlist_tracks(sp, playlist_id):
    """Get all tracks from the specified playlist."""
    try:
        tracks = sp.playlist_tracks(playlist_id, fields="items(track(uri))")["items"]
        logger.info(f"Retrieved {len(tracks)} tracks from playlist {playlist_id}")
        return [track["track"]["uri"] for track in tracks]
    except SpotifyException as e:
        logger.error(f"Failed to get playlist tracks: {e}")
        return []


def add_tracks_to_playlist(sp, playlist_id, track_uris):
    """Add the specified tracks to the destination playlist."""
    try:
        sp.playlist_add_items(playlist_id, track_uris)
        logger.info(f"Added {len(track_uris)} tracks to playlist {playlist_id}")
    except SpotifyException as e:
        logger.error(f"Failed to add tracks to playlist: {e}")


def get_track_names(sp, track_uris):
    """Get the names of the specified tracks."""
    try:
        tracks = sp.tracks(track_uris)["tracks"]
        logger.info(f"Retrieved names for {len(tracks)} tracks")
        return [{"artist": track["artists"][0]["name"], "name": track["name"]} for track in tracks]
    except SpotifyException as e:
        logger.error(f"Failed to get track names: {e}")
        return []
