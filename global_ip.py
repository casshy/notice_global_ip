# -*- coding: utf-8 -*-

import requests

url = 'http://ipecho.net/plain'

def get_global_ip():
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return ""


if __name__ == "__main__":
    print(get_global_ip())
