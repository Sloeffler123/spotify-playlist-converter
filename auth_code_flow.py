import random
import base64
import requests
import webbrowser
from my_server import make_socket, parse_code

def request_user_authorization(authorize_url, client_id, redirect_uri, port, ip_address):
    random_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    ran_string = "".join([random.choice(random_string) for _ in range(16)])
    state = ran_string
    scope = "playlist-modify-public playlist-modify-private"
    query_params = {
        "client_id": client_id, 
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "state": state,
        "scope": scope
    }
    resp = requests.get(url=authorize_url, params=query_params)
    webbrowser.open(resp.url)
    code = make_socket(port, ip_address)
    final_token = parse_code(code)
    return final_token

def request_access_token(code_recieved, redirect_uri, client_id, client_secret, access_url):
    body_params = {
        "grant_type": "authorization_code",
        "code": code_recieved,
        "redirect_uri": redirect_uri
    }
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
        "content-type": "application/x-www-form-urlencoded"
    }
    access_res = requests.post(url=access_url, params=body_params, headers=headers)
    return access_res.json()["access_token"]