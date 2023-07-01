#!/bin/bash
# sends POST request and two variables and display the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
