#!/bin/bash
# Bash script that DELETE request to URL passed as first argument and displays body
curl -sLX DELETE "$1"
