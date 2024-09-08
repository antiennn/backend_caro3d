import requests


def get_access_token(access_token):
    return requests.get("https://graph.facebook.com/me?access_token=" + access_token).json()