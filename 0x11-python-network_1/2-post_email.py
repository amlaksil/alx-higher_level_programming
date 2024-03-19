#!/usr/bin/python3
"""
This module provides a way to send a POST request to a specified URL
with an email address and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
import sys

if __name__ == '__main__':
    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    # Create a POST request object
    req = urllib.request.Request(sys.argv[1], data=data, method='POST')

    # Send the request and handle the response
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(data.decode('utf-8'))
