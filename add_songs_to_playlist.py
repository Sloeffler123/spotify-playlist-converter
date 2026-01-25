import requests

def add_songs(songs_lst: list[list], access_token, new_playlist_url):
    for songs in songs_lst:

        data = {
            "uris": songs
        }
        header = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        resp = requests.post(url=new_playlist_url, headers=header, json=data)
        print(resp.json())