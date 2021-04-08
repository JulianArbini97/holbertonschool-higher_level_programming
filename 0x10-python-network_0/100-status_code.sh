#!/bin/bash
# comment
curl -so /dev/null -Iw "%{http_code}" "$1" 
