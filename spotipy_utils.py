import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_spotify_client(client_id, client_secret, redirect_uri):
    """Create a new instance of the Spotipy client with authentication."""
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                     client_secret=client_secret,
                                                     redirect_uri=redirect_uri,
                                                     scope="playlist-modify-private"))

def get_playlist_tracks(sp, playlist_id):
    """Get all tracks from the specified playlist."""
    tracks = sp.playlist_tracks(playlist_id, fields="items(track(uri))")["items"]
    return [track["track"]["uri"] for track in tracks]

def add_tracks_to_playlist(sp, playlist_id, track_uris):
    """Add the specified tracks to the destination playlist."""
    sp.playlist_add_items(playlist_id, track_uris)

def get_track_names(sp, track_uris):
    """Get the names of the specified tracks."""
    tracks = sp.tracks(track_uris)["tracks"]
    return [{"artist": track["artists"][0]["name"], "name": track["name"]} for track in tracks]
