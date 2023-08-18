#!/bin/sh

currentVersion="$(cat intellij-idea-ultimate.spec | grep Version: | awk '{print $2}')"
currentBuildId="$(cat intellij-idea-ultimate.spec | grep '%global build_id' | awk '{print $3}')"

apiResponse="$(curl -s 'https://data.services.jetbrains.com/products/releases?code=IIU&latest=true&type=release')"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.IIU[0].version')"
latestBuildId="$(printf "%s" "${apiResponse}" | jq -r '.IIU[0].build')"

echo "Current version: $currentVersion build: $currentBuildId"
echo "Latest version: $latestVersion build: $latestBuildId"


if [ "$currentBuildId" != "$latestBuildId" ]; then
	DATE="$(date "+%a %b %d %Y")"
	USER="RPM Bot <rpm-bot@coder966.net>"


	sed -i "s/^Version: .*/Version:       ${latestVersion}/" intellij-idea-ultimate.spec
	sed -i "s/^%global *build_id .*/%global build_id ${latestBuildId}/" intellij-idea-ultimate.spec
	sed -i "s/^%changelog/%changelog\n\* ${DATE} ${USER} - ${latestVersion}\n- Update to ${latestVersion}\n/" intellij-idea-ultimate.spec


	git commit intellij-idea-ultimate.spec -m "Update to ${latestVersion}"
	git push
fi
