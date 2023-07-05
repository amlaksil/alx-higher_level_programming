#!/bin/bash
# send request to the URL passed and display the status code of the response only
curl --head "$1" | awk '/^HTTP/{print $2}'
