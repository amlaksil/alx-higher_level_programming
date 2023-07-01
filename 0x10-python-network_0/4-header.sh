#!/bin/bash
# sends a GET request and set header variable 'X-School-User-Id' to a value 98
curl -s "$1" -H "X-School-User-Id: 98"
