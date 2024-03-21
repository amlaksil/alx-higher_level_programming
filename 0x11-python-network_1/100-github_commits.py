#!/usr/bin/python3
"""
This script retrieves the latest commits from a GitHub repository using the
GitHub API. It takes the repository name and owner name as command-line
arguments. The script uses the requests package to make HTTP requests and
retrieves the commits' SHA and author name.

Usage: python3 100-github_commits.py <repository> <owner>

Arguments:
    repo (str): The name of the repository.
    owner (str): The owner of the repository.
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
