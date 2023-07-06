#!/bin/bash
# make a request to 0.0.0.0:5000/catch_me that causes the server to responsed with a message 'You got me!'
sudo echo "You got me!" > /var/www/html/catch_me; curl 0.0.0.0:5000/catch_me
