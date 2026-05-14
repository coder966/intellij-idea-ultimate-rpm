#!/bin/sh

apiResponse="$(curl -s "https://data.services.jetbrains.com/products/releases?code=IIU&latest=true&type=release")"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.IIU[0].version')"

echo $latestVersion
