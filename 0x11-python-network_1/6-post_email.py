#!/usr/bin/python3
"""
This module provides a way to send a POST request to a specified URL
with an email address and displays the body of the response.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}

    response = requests.post(url, data=payload)
    print(response.text)
