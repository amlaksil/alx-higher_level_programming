#!/usr/bin/python3
"""
This script takes a letter as an argument and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q.
If no argument is given, q is set to an empty string ("").
If the response body is properly JSON formatted and not empty, it displays
the id and name in the format: [<id>] <name>.
Otherwise, it displays:
- "Not a valid JSON" if the JSON is invalid.
- "No result" if the JSON is empty.
"""
import requests
import sys

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': letter}
    url = f'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
