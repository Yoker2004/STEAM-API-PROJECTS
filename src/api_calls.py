import requests
# import json

def get_games(steam_id, api_key):
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    parameters = {
        "key": api_key,
        "steamid": steam_id,
        "include_appinfo": True,

    }
    return requests.get(url, params=parameters).json()