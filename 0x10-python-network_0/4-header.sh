#!/bin/bash
# sends a GET request to the URL passed and set header variable
# 'X-School-User-Id' to a value 98 and display the response
curl -s "$1" -H "X-School-User-Id: 98"
