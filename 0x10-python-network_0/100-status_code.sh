#!/bin/bash
# This script displays only the status code of the response
curl -s -X HEAD -w "%{http_code}" "$1"
