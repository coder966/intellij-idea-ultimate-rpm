Name:          keystore-explorer
Version:       5.7.0
Release:       1%{?dist}
Summary:       KeyStore Explorer
License:       GPL-3.0-or-later
URL:           https://keystore-explorer.org/
Packager:      Khalid Alharisi <coder966@gmail.com>

%define version_no_dots %(echo %{version} | tr -d '.')
Source0:       https://github.com/kaikramer/keystore-explorer/releases/download/v%{version}/kse-%{version_no_dots}.zip
Source1:       keystore-explorer.desktop


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}



%description
KeyStore Explorer is a free GUI replacement for the Java command-line utilities keytool and jarsigner.



%prep
unzip -q %{SOURCE0}


%setup -q -T -D -n kse-%{version_no_dots}


%build



%install


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 icons/kse_512.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

cp %{SOURCE1} %{name}.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop



%files
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Mon Aug 24 2026 RPM Bot <rpm-bot@coder966.net> - 5.7.0
- Update to 5.7.0

* Sat Jun 13 2026 RPM Bot <rpm-bot@coder966.net> - 5.6.1
- Update to 5.6.1

* Fri Jun 12 2026 RPM Bot <rpm-bot@coder966.net> - null
- Update to null

* Tue May 19 2026 RPM Bot <rpm-bot@coder966.net> - 5.6.1
- Update to 5.6.1
