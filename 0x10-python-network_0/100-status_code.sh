#!/bin/bash
# send request to the URL passed and display the status code of the response only
curl -so /dev/null -w "%{http_code}" "$1"
