#!/usr/bin/python3
"""
Make request to `https://alx-intranet.hbtn.io/status`
and format the body of the response.
"""
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()

    print(f"Body response:\n\t- type: {type(data)}\n\t- content: {data}" +
          f"\n\t- utf8 content: {data.decode('utf-8')}")
