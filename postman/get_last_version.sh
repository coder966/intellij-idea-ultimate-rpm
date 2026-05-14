#!/bin/sh

apiResponse="$(curl -s 'https://www.postman.com/mkapi/release.json')"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.notes[0].version')"

echo $latestVersion
