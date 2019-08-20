#!/bin/bash
# This script sends a GET with a header variable and displays the response
curl -s -X GET --header "X-HolbertonSchool-User-Id: 98" "$1"
