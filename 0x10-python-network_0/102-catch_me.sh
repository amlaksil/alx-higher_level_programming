#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me that causes the server to responsed with a message 'You got me!'
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:You got me!"
