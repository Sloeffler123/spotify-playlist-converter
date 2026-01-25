import requests

def get_token(client_id, client_secret, token_url):
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(token_url, data=data, headers=headers)
    token_response = response.json()
    return token_response["access_token"]