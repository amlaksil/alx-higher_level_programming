#!/bin/bash
# send request to the URL passed and display the status code of the response only
curl --silent --output /dev/null --write-out "%{http_code}" "$1"
