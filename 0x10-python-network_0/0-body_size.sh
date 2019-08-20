#!/bin/bash
# This script displays the size of the body of http response
curl -sw "%{size_download}\n" 34.206.234.184:46075 | sed 's/[^0-9]*//g'
