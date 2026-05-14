#!/bin/sh

appDirNameArg="$1"

echo "Checking for updates for ${appDirNameArg}"

currentVersion="$(cat ${appDirNameArg}/rpm.spec | grep Version: | awk '{print $2}')"

latestVersion="$(sh "./$appDirNameArg/get_last_version.sh")"

echo "Current version: $currentVersion"
echo "Latest version: $latestVersion"


if [ "$currentVersion" != "$latestVersion" ]; then
	echo "New version available: $latestVersion. Updating..."

	DATE="$(date "+%a %b %d %Y")"
	USER="RPM Bot <rpm-bot@coder966.net>"


	sed -i "s/^Version: .*/Version:       ${latestVersion}/" ${appDirNameArg}/rpm.spec
	sed -i "s/^%changelog/%changelog\n\* ${DATE} ${USER} - ${latestVersion}\n- Update to ${latestVersion}\n/" ${appDirNameArg}/rpm.spec


	git commit ${appDirNameArg}/rpm.spec -m "Update to ${latestVersion}"
	git push
fi
