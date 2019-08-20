#!/bin/bash
# This sends a POST request with email and subject data and displays response
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
