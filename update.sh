#!/bin/sh

appDirNameArg="$1"
apiUrlArg="$2"

echo "Checking for updates for ${appDirNameArg} using API: ${apiUrlArg}"

currentVersion="$(cat ${appDirNameArg}/rpm.spec | grep Version: | awk '{print $2}')"
currentBuildId="$(cat ${appDirNameArg}/rpm.spec | grep '%global build_id' | awk '{print $3}')"

apiResponse="$(curl -s "${apiUrlArg}")"
latestVersion="$(printf "%s" "${apiResponse}" | jq -r '.IIU[0].version')"
latestBuildId="$(printf "%s" "${apiResponse}" | jq -r '.IIU[0].build')"

echo "Current version: $currentVersion build: $currentBuildId"
echo "Latest version: $latestVersion build: $latestBuildId"


if [ "$currentBuildId" != "$latestBuildId" ]; then
	DATE="$(date "+%a %b %d %Y")"
	USER="RPM Bot <rpm-bot@coder966.net>"


	sed -i "s/^Version: .*/Version:       ${latestVersion}/" ${appDirNameArg}/rpm.spec
	sed -i "s/^%global *build_id .*/%global build_id ${latestBuildId}/" ${appDirNameArg}/rpm.spec
	sed -i "s/^%changelog/%changelog\n\* ${DATE} ${USER} - ${latestVersion}\n- Update to ${latestVersion}\n/" ${appDirNameArg}/rpm.spec


	git commit ${appDirNameArg}/rpm.spec -m "Update to ${latestVersion}"
	git push
fi
