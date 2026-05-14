Name:          soapui
Version:       5.7.1
Release:       2%{?dist}
Summary:       SoapUI
License:       Apache 2.0
URL:           https://www.soapui.com/
Packager:      Khalid Alharisi <coder966@gmail.com>


Source0:       https://dl.eviware.com/soapuios/%{version}/SoapUI-%{version}-linux-bin.tar.gz
Source1:       soapui.desktop
Source2:       https://raw.githubusercontent.com/SmartBear/soapui/next/soapui/src/main/resources/com/eviware/soapui/resources/images/SoapUI-OS_256-256.png


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}



%description
SoapUI




%prep


# SoapUI-%{version} is the dir inside the tar
%setup -q -n SoapUI-%{version}


%build



%install


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 %{SOURCE2} %{buildroot}/opt/%{name}/icon.png

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}




%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*




%changelog

* Tue Aug 18 2023 coder966 <coder966@gmail.com> - 5.7.1
- Initial Release
