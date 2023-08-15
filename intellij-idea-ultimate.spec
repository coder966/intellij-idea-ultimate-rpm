Name:          intellij-idea-ultimate
Version:       2023.2
Release:       1%{?dist}
Summary:       IntelliJ IDEA Ultimate
License:       Apache 2.0
URL:           https://www.jetbrains.com/idea/

Source0:       https://download.jetbrains.com/idea/ideaIU-%{version}.tar.gz
Source1:       https://raw.githubusercontent.com/coder966/intellij-idea-ultimate-rpm/master/intellij-idea-ultimate.desktop


BuildRequires: desktop-file-utils


%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}


%global build_id 232.8660.185




%description
IntelliJ IDEA Ultimate




%prep


# idea-IU-%{build_id} is the dir inside the tar
%setup -q -n idea-IU-%{build_id}


%build



%install
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
* Tue Aug 15 2023 coder966 <coder966@gmail.com> - 2023.2
- Initial Release
