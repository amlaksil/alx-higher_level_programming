#!/bin/bash
# sends a DELETE request to the URL passed and display the body of the response
curl -s "$1" -X DELETE
