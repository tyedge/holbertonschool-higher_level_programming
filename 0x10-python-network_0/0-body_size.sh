#!/bin/bash
# This script displays the size of the body of http response
curl -sw "%{size_download}\n" "$1" | sed 's/[^0-9]*//g'
