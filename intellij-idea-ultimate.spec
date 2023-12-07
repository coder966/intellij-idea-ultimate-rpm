Name:          intellij-idea-ultimate
Version:       2023.3
Release:       1%{?dist}
Summary:       IntelliJ IDEA Ultimate
License:       Apache 2.0
URL:           https://www.jetbrains.com/idea/
Packager:      Khalid Alharisi <coder966@gmail.com>


Source0:       https://download.jetbrains.com/idea/ideaIU-%{version}.tar.gz
Source1:       https://raw.githubusercontent.com/coder966/intellij-idea-ultimate-rpm/master/intellij-idea-ultimate.desktop


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}


%global build_id 233.11799.241


%description
IntelliJ IDEA Ultimate




%prep


# idea-IU-%{build_id} is the dir inside the tar
%setup -q -n idea-IU-%{build_id}


%build



%install

# Remove files for different architectures
rm -rf lib/pty4j/linux/{aarch64,arm,mips64el,ppc64le,x86}
rm -rf plugins/cwm-plugin/quiche-native/linux-aarch64
rm -rf plugins/cwm-plugin/quiche-native/{darwin,win}*
rm -rf plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-{darwin-amd64,darwin-arm64,linux-arm64,windows-amd64,windows-arm64}
rm -rf plugins/maven/lib/maven3/lib/jansi-native/{freebsd32,freebsd64,linux32,osx,windows32,windows64}
rm -rf plugins/Kotlin/bin/{macos,windows}
rm -rf plugins/webp/lib/libwebp/linux/libwebp_jni.so
rm -rf plugins/webp/lib/libwebp/{mac,win}


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/idea.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/idea.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}




%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*




%changelog
* Thu Dec 07 2023 RPM Bot <rpm-bot@coder966.net> - 2023.3
- Update to 2023.3

* Fri Nov 10 2023 RPM Bot <rpm-bot@coder966.net> - 2023.2.5
- Update to 2023.2.5

* Thu Oct 26 2023 RPM Bot <rpm-bot@coder966.net> - 2023.2.4
- Update to 2023.2.4

* Thu Oct 12 2023 RPM Bot <rpm-bot@coder966.net> - 2023.2.3
- Update to 2023.2.3

* Thu Sep 14 2023 RPM Bot <rpm-bot@coder966.net> - 2023.2.2
- Update to 2023.2.2

* Thu Aug 24 2023 RPM Bot <rpm-bot@coder966.net> - 2023.2.1
- Update to 2023.2.1

* Tue Aug 15 2023 coder966 <coder966@gmail.com> - 2023.2
- Initial Release
