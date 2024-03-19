#!/usr/bin/python3
"""
Make request to `https://alx-intranet.hbtn.io/status`
and format the body of the response.
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print(
        f'Body response:\n\t- type: {type(res.text)}\n\t- content: {res.text}')
