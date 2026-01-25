import requests

def fetch_playlist(main_playlist_url, initial_token):
    header = {
        "Authorization": f"Bearer {initial_token}"
    }
    response = requests.get(url=main_playlist_url, headers=header)
    data = response.json()
    return data
