Name:          intellij-idea-ultimate
Version:       2025.2.1
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


%global build_id 252.25557.131


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
* Fri Aug 29 2025 RPM Bot <rpm-bot@coder966.net> - 2025.2.1
- Update to 2025.2.1

* Tue Aug 05 2025 RPM Bot <rpm-bot@coder966.net> - 2025.2
- Update to 2025.2

* Sat Jul 26 2025 RPM Bot <rpm-bot@coder966.net> - 2025.1.4.1
- Update to 2025.1.4.1

* Tue Jun 24 2025 RPM Bot <rpm-bot@coder966.net> - 2025.1.3
- Update to 2025.1.3

* Thu Jun 05 2025 RPM Bot <rpm-bot@coder966.net> - 2025.1.2
- Update to 2025.1.2

* Sat May 10 2025 RPM Bot <rpm-bot@coder966.net> - 2025.1.1.1
- Update to 2025.1.1.1

* Thu May 08 2025 RPM Bot <rpm-bot@coder966.net> - 2025.1.1
- Update to 2025.1.1

* Wed Apr 16 2025 RPM Bot <rpm-bot@coder966.net> - 2025.1
- Update to 2025.1

* Tue Mar 18 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.5
- Update to 2024.3.5

* Thu Mar 06 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.4.1
- Update to 2024.3.4.1

* Fri Feb 28 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.4
- Update to 2024.3.4

* Thu Feb 13 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.3
- Update to 2024.3.3

* Thu Jan 30 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.2.2
- Update to 2024.3.2.2

* Fri Jan 24 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.2.1
- Update to 2024.3.2.1

* Fri Jan 17 2025 RPM Bot <rpm-bot@coder966.net> - 2024.3.2
- Update to 2024.3.2

* Thu Dec 19 2024 RPM Bot <rpm-bot@coder966.net> - 2024.3.1.1
- Update to 2024.3.1.1

* Tue Dec 10 2024 RPM Bot <rpm-bot@coder966.net> - 2024.3.1
- Update to 2024.3.1

* Thu Nov 14 2024 RPM Bot <rpm-bot@coder966.net> - 2024.3
- Update to 2024.3

* Thu Oct 24 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2.4
- Update to 2024.2.4

* Thu Sep 26 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2.3
- Update to 2024.2.3

* Thu Sep 19 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2.2
- Update to 2024.2.2

* Fri Aug 30 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2.1
- Update to 2024.2.1

* Wed Aug 21 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2.0.2
- Update to 2024.2.0.2

* Wed Aug 14 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2.0.1
- Update to 2024.2.0.1

* Wed Aug 07 2024 RPM Bot <rpm-bot@coder966.net> - 2024.2
- Update to 2024.2

* Tue Aug 06 2024 RPM Bot <rpm-bot@coder966.net> - 2024.1.5
- Update to 2024.1.5

* Fri Jun 21 2024 RPM Bot <rpm-bot@coder966.net> - 2024.1.4
- Update to 2024.1.4

* Tue Jun 11 2024 RPM Bot <rpm-bot@coder966.net> - 2024.1.3
- Update to 2024.1.3

* Fri May 24 2024 RPM Bot <rpm-bot@coder966.net> - 2024.1.2
- Update to 2024.1.2

* Tue Apr 30 2024 RPM Bot <rpm-bot@coder966.net> - 2024.1.1
- Update to 2024.1.1

* Thu Apr 04 2024 RPM Bot <rpm-bot@coder966.net> - 2024.1
- Update to 2024.1

* Fri Mar 22 2024 RPM Bot <rpm-bot@coder966.net> - 2023.3.6
- Update to 2023.3.6

* Wed Mar 13 2024 RPM Bot <rpm-bot@coder966.net> - 2023.3.5
- Update to 2023.3.5

* Wed Feb 14 2024 RPM Bot <rpm-bot@coder966.net> - 2023.3.4
- Update to 2023.3.4

* Fri Jan 26 2024 RPM Bot <rpm-bot@coder966.net> - 2023.3.3
- Update to 2023.3.3

* Thu Dec 21 2023 RPM Bot <rpm-bot@coder966.net> - 2023.3.2
- Update to 2023.3.2

* Wed Dec 13 2023 RPM Bot <rpm-bot@coder966.net> - 2023.3.1
- Update to 2023.3.1

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
