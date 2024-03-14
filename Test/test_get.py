import unittest
from Infra.api_wrapper import APIWrapper
from Logic.spotify_logic import Spotify


class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.token = self.my_api.get_token()
        self.headers = self.my_api.get_auth_header(self.token)
        self.api_logic = Spotify(self.token, self.my_api)

    def test_get_artist(self, artist_name="Radiohead"):
        result = self.api_logic.search_for_artist(self.token, artist_name)
        artist_name_result = result["name"]
        self.assertEqual(artist_name, artist_name_result, "Wrong Artist ")

    def test_get_album(self, artist_album="OK Computer"):
        result = self.api_logic.search_for_album(self.token, artist_album)
        album_name_result = result["name"]
        self.assertEqual(artist_album, album_name_result, "Wrong Album ")


'''

# create playlist
def create_playlist(token, user_id, playlist_name, public=True, description=""):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "name": playlist_name,
        "public": public,
        "description": description
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        playlist_id = response.json()["id"]
        print(f"Playlist '{playlist_name}' created successfully with ID: {playlist_id}")
        return playlist_id
    else:
        print(f"Error creating playlist: {response.status_code}, {response.text}")
        return None



playlist_id = create_playlist(token, user_id, "Test Playlist", True, "Testing Create Playlist")

songs = get_songs_by_artist(token, artist_id)

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")

print("============================================")

album_tracks = get_album_tracks(token, album_id)

for idx, album_track in enumerate(album_tracks):
    print(f"{idx + 1}. {album_track['name']}")
'''
