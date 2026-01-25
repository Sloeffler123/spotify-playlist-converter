from get_playlist import fetch_playlist

def main_loop(main_playlist_url, initial_token):
    url = main_playlist_url
    songs = []    
    while True:
        data = fetch_playlist(url, initial_token)
        go_through_loop(data, songs)
        url = get_next_playlist(data)
        if url:
            continue
        else:
            break
    return songs
    
def get_next_playlist(data):
    return data["next"]

def go_through_loop(data, songs_lst):
    lst = []
    for i in data["items"]:
        uri = i["track"]["uri"]
        lst.append(uri)
    songs_lst.append(lst)