#!/bin/bash
#This script sends a JSON POST request to a URL and displays the body
curl -sH "Content-Type: application/json" -d "@$2" -X POST "$1"
