import os 
from dotenv import load_dotenv
from get_initial_token import get_token

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
MAIN_PLAYLIST_ID = os.getenv("MAIN_PLAYLIST_ID")
NEW_PLAYLIST_ID = os.getenv("NEW_PLAYLIST_ID")
IP_ADDRESS = os.getenv("IP_ADDRESS")
PORT = os.getenv("PORT")
MAIN_PLAYLIST_URL = f"https://api.spotify.com/v1/playlists/{MAIN_PLAYLIST_ID}/tracks?market=PK&fields=items%28track%28name%2Curi%29%2Cartists%28name%29%29%2Cnext"
NEW_PLAYLIST_URL = f"https://api.spotify.com/v1/playlists/{NEW_PLAYLIST_ID}/tracks"
AUTHORIZE_URL = f"https://accounts.spotify.com/authorize?"
ACCESS_URL = f"https://accounts.spotify.com/api/token"
INITIAL_TOKEN = get_token(CLIENT_ID, CLIENT_SECRET, ACCESS_URL)
