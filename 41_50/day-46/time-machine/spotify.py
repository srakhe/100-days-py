import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']
USER = os.environ['SPOTIFY_USER_ID']


def create_playlist(date):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri="http://localhost:8080",
                                                   scope='playlist-modify-public'))

    playlist = sp.user_playlist_create(user=USER, name=str(date) + ' Billboard 100',
                                       description='Take me back in time!')
    play_id = playlist['id']

    return play_id


def add_songs_to_playlist(playlist_id, songs, artists):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri="http://localhost:8080",
                                                   scope='playlist-modify-public'))

    track_uris = []
    for song, artist in zip(songs, artists):
        track_id = sp.search(q='artist:' + artist + ' track:' + song, type='track')
        if track_id['tracks']['items']:
            track_uris.append(track_id['tracks']['items'][0]['uri'])

    if sp.playlist_add_items(playlist_id, track_uris):
        return True
