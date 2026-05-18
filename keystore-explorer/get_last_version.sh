#!/bin/sh

apiResponse="$(curl -s 'https://api.github.com/repos/kaikramer/keystore-explorer/releases/latest')"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.tag_name' | sed -e 's/v//g')"

echo $latestVersion
