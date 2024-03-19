#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import urllib
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e}')
