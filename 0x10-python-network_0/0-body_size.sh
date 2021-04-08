#!/bin/bash
# Bash script takes URL, sends GET URL, displays body of response
curl -sI "$1" | grep Content-Length | awk '{print $2}'
