#!/bin/bash
# Sends a Json POST request to a URL passed as the first argument and display the body of the response
curl -s "$1" -d "@$2" -X POST --header "Content-Type:application/json"
