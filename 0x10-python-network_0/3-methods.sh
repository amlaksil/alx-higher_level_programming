#!/bin/bash
# displays all HTPP methods the server will accept
curl -sI "$1" -X OPTIONS | grep 'Allow:' | cut -d " " -f 2-
