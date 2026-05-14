Name:          visualvm
Version:       2.2.1
Release:       1%{?dist}
Summary:       Visual VM
License:       GPL-2.0-or-later
URL:           https://visualvm.github.io/
Packager:      Khalid Alharisi <coder966@gmail.com>

%define version_no_dots %(echo %{version} | tr -d '.')
Source0:       https://github.com/oracle/visualvm/releases/download/%{version}/visualvm_%{version_no_dots}.zip
Source1:       visualvm.desktop
Source2:       https://raw.githubusercontent.com/oracle/visualvm/master/integrations/vscode/images/extension_icon.png


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}



%description
Visual VM




%prep
unzip -q %{SOURCE0}


%setup -q -T -D -n visualvm_%{version_no_dots}


%build



%install


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 %{SOURCE2} %{buildroot}/opt/%{name}/icon.png

cp %{SOURCE1} %{name}.desktop
sed -i 's/@VERSION@/%{version}/g' %{name}.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop



%files
/opt/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Fri May 15 2026 RPM Bot <rpm-bot@coder966.net> - 2.2.1
- Update to 2.2.1
