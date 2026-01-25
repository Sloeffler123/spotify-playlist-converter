from loop_through_playlist import main_loop
from auth_code_flow import request_access_token, request_user_authorization
from add_songs_to_playlist import add_songs
from constants import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, INITIAL_TOKEN, IP_ADDRESS, PORT, MAIN_PLAYLIST_URL, NEW_PLAYLIST_URL, ACCESS_URL, AUTHORIZE_URL

def main():
    list_of_songs = main_loop(MAIN_PLAYLIST_URL, INITIAL_TOKEN)
    access_token = request_user_authorization(AUTHORIZE_URL, CLIENT_ID, REDIRECT_URI, PORT, IP_ADDRESS)
    final_access_token = request_access_token(access_token, REDIRECT_URI, CLIENT_ID, CLIENT_SECRET, ACCESS_URL)
    add_songs(list_of_songs, final_access_token, NEW_PLAYLIST_URL)

if __name__ == "__main__":
    main()
