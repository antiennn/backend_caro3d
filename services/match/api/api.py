import requests


def get_current_user(access_token):
    return requests.get("http://127.0.0.1:8000/api/users/auth/?access_token=" + access_token).json()