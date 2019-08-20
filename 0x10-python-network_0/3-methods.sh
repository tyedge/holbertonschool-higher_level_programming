#!/bin/bash
# This script displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | sed -n -e '/Allow/ s/.*\: *//p'
