#!/bin/sh

apiResponse="$(curl -s 'https://api.github.com/repos/oracle/visualvm/releases/latest')"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.tag_name' | sed -e 's/v//g')"

echo $latestVersion
