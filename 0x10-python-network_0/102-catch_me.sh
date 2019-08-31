#!/bin/bash
# This script requests 0.0.0.0:5000/catch_me to respond with You got me!
curl -sL --request PUT "0.0.0.0:5000/catch_me" --header "Origin: HolbertonSchool" --data "user_id"=98
