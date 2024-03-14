import json

class Spotify:

    URL = "https://api.spotify.com/v1/search"

    def __init__(self, token, api_object):
        self.api = api_object
        self.token = token

    def search_for_artist(self,token, artist_name):
        url = "https://api.spotify.com/v1/search"
        query = f"?q={artist_name}&type=artist&limit=13"

        query_url = url + query
        result = self.api.api_get_request(query_url,token)
        json_result = json.loads(result.content)["artists"]["items"]

        if len(json_result) == 0:
            print("No artist Found")
            return None
        return json_result[0]

    def search_for_album(self, token, album_name):
        url = "https://api.spotify.com/v1/search"
        query = f"?q={album_name}&type=album&limit=13"

        query_url = url + query
        result = self.api.api_get_request(query_url,token)

        if result.status_code == 200:
            json_result = result.json()["albums"]["items"]
            if len(json_result) == 0:
                print("No albums found for the specified name.")
                return None
            return json_result[0]  # Return the first album in the list
        else:
            print(f"Error: {result.status_code}, {result.text}")
            return None

    def get_songs_by_artist(self, token, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
        result = self.api.api_get_request(url,token)
        json_result = json.loads(result.content)["tracks"]
        return json_result

    def get_album_tracks(self, token, album_id):
        url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
        result = self.api.api_get_request(url,token)
        json_result = json.loads(result.content)["items"]
        return json_result
