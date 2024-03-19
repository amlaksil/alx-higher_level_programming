#!/usr/bin/python3
"""
This script takes your GitHub username and personal access token as arguments
and uses Basic Authentication to access the GitHub API and display your
user ID.
Arguments:
    <username>: Your GitHub username.
    <token>: Your personal access token (PAT) for authentication
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
