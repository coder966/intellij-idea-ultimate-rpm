Name:          postman
Version:       12.11.2
Release:       1%{?dist}
Summary:       Postman
License:       Commercial
URL:           https://www.postman.com/
Packager:      Khalid Alharisi <coder966@gmail.com>


Source0:       https://dl.pstmn.io/download/version/%{version}/linux_64
Source1:       postman.desktop


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}



%description
Postman is a comprehensive API (Application Programming Interface) platform that simplifies every step of the API lifecycle.
It allows developers to design, mock, debug, test, document, and monitor APIs from a single environment.




%prep


# Postman/app is the dir inside the tar
%setup -q -n Postman/app


%build



%install


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 resources/app/assets/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}




%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*




%changelog
* Tue May 19 2026 RPM Bot <rpm-bot@coder966.net> - 12.11.2
- Update to 12.11.2

* Mon May 18 2026 RPM Bot <rpm-bot@coder966.net> - 12.11.0
- Update to 12.11.0

* Fri May 15 2026 RPM Bot <rpm-bot@coder966.net> - 12.10.6
- Update to 12.10.6

* Thu May 14 2026 RPM Bot <rpm-bot@coder966.net> - 12.10.5
- Update to 12.10.5

* Wed May 13 2026 RPM Bot <rpm-bot@coder966.net> - 12.10.2
- Update to 12.10.2

* Mon May 11 2026 RPM Bot <rpm-bot@coder966.net> - 12.10.0
- Update to 12.10.0

* Fri May 08 2026 RPM Bot <rpm-bot@coder966.net> - 12.9.7
- Update to 12.9.7

* Tue May 05 2026 RPM Bot <rpm-bot@coder966.net> - 12.9.2
- Update to 12.9.2

* Mon May 04 2026 RPM Bot <rpm-bot@coder966.net> - 12.9.0
- Update to 12.9.0

* Thu Apr 30 2026 RPM Bot <rpm-bot@coder966.net> - 12.8.4
- Update to 12.8.4

* Wed Apr 29 2026 RPM Bot <rpm-bot@coder966.net> - 12.8.3
- Update to 12.8.3

* Tue Apr 28 2026 RPM Bot <rpm-bot@coder966.net> - 12.8.1
- Update to 12.8.1

* Fri Apr 24 2026 RPM Bot <rpm-bot@coder966.net> - 12.7.6
- Update to 12.7.6

* Thu Apr 23 2026 RPM Bot <rpm-bot@coder966.net> - 12.7.5
- Update to 12.7.5

* Wed Apr 22 2026 RPM Bot <rpm-bot@coder966.net> - 12.7.4
- Update to 12.7.4

* Tue Apr 21 2026 RPM Bot <rpm-bot@coder966.net> - 12.7.1
- Update to 12.7.1

* Mon Apr 20 2026 RPM Bot <rpm-bot@coder966.net> - 12.7.0
- Update to 12.7.0

* Sat Apr 18 2026 RPM Bot <rpm-bot@coder966.net> - 12.6.8
- Update to 12.6.8

* Wed Apr 15 2026 RPM Bot <rpm-bot@coder966.net> - 12.6.3
- Update to 12.6.3

* Tue Apr 14 2026 RPM Bot <rpm-bot@coder966.net> - 12.6.1
- Update to 12.6.1

* Fri Apr 10 2026 RPM Bot <rpm-bot@coder966.net> - 12.5.6
- Update to 12.5.6

* Thu Apr 09 2026 RPM Bot <rpm-bot@coder966.net> - 12.5.5
- Update to 12.5.5

* Wed Apr 08 2026 RPM Bot <rpm-bot@coder966.net> - 12.5.2
- Update to 12.5.2

* Tue Mar 10 2026 RPM Bot <rpm-bot@coder966.net> - 12.1.1
- Update to 12.1.1

* Sat Mar 07 2026 RPM Bot <rpm-bot@coder966.net> - 12.0.8
- Update to 12.0.8

* Thu Mar 05 2026 RPM Bot <rpm-bot@coder966.net> - 12.0.5
- Update to 12.0.5

* Tue Mar 03 2026 RPM Bot <rpm-bot@coder966.net> - 12.0.3
- Update to 12.0.3

* Mon Mar 02 2026 RPM Bot <rpm-bot@coder966.net> - 12.0.1
- Update to 12.0.1

* Sun Mar 01 2026 RPM Bot <rpm-bot@coder966.net> - 11.86.1
- Update to 11.86.1

* Tue Feb 17 2026 RPM Bot <rpm-bot@coder966.net> - 11.85.1
- Update to 11.85.1

* Fri Feb 13 2026 RPM Bot <rpm-bot@coder966.net> - 11.84.3
- Update to 11.84.3

* Wed Feb 11 2026 RPM Bot <rpm-bot@coder966.net> - 11.84.2
- Update to 11.84.2

* Tue Feb 03 2026 RPM Bot <rpm-bot@coder966.net> - 11.83.2
- Update to 11.83.2

* Sat Jan 31 2026 RPM Bot <rpm-bot@coder966.net> - 11.82.6
- Update to 11.82.6

* Fri Jan 30 2026 RPM Bot <rpm-bot@coder966.net> - 11.82.5
- Update to 11.82.5

* Tue Jan 27 2026 RPM Bot <rpm-bot@coder966.net> - 11.82.1
- Update to 11.82.1

* Sat Jan 24 2026 RPM Bot <rpm-bot@coder966.net> - 11.81.4
- Update to 11.81.4

* Fri Jan 23 2026 RPM Bot <rpm-bot@coder966.net> - 11.81.3
- Update to 11.81.3

* Wed Jan 21 2026 RPM Bot <rpm-bot@coder966.net> - 11.81.1
- Update to 11.81.1

* Tue Jan 20 2026 RPM Bot <rpm-bot@coder966.net> - 11.81.0
- Update to 11.81.0

* Fri Jan 16 2026 RPM Bot <rpm-bot@coder966.net> - 11.80.4
- Update to 11.80.4

* Thu Jan 15 2026 RPM Bot <rpm-bot@coder966.net> - 11.80.3
- Update to 11.80.3

* Wed Jan 14 2026 RPM Bot <rpm-bot@coder966.net> - 11.80.2
- Update to 11.80.2

* Mon Jan 12 2026 RPM Bot <rpm-bot@coder966.net> - 11.80.0
- Update to 11.80.0

* Fri Jan 09 2026 RPM Bot <rpm-bot@coder966.net> - 11.79.5
- Update to 11.79.5

* Thu Jan 08 2026 RPM Bot <rpm-bot@coder966.net> - 11.79.4
- Update to 11.79.4

* Wed Jan 07 2026 RPM Bot <rpm-bot@coder966.net> - 11.79.3
- Update to 11.79.3

* Tue Jan 06 2026 RPM Bot <rpm-bot@coder966.net> - 11.79.1
- Update to 11.79.1

* Wed Dec 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.77.2
- Update to 11.77.2

* Mon Dec 22 2025 RPM Bot <rpm-bot@coder966.net> - 11.77.0
- Update to 11.77.0

* Fri Dec 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.76.9
- Update to 11.76.9

* Wed Dec 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.76.5
- Update to 11.76.5

* Tue Dec 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.76.0
- Update to 11.76.0

* Fri Dec 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.75.6
- Update to 11.75.6

* Thu Dec 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.75.4
- Update to 11.75.4

* Mon Dec 08 2025 RPM Bot <rpm-bot@coder966.net> - 11.75.1
- Update to 11.75.1

* Fri Dec 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.74.5
- Update to 11.74.5

* Thu Dec 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.74.4
- Update to 11.74.4

* Wed Dec 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.74.2
- Update to 11.74.2

* Fri Nov 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.73.5
- Update to 11.73.5

* Wed Nov 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.73.3
- Update to 11.73.3

* Sat Nov 22 2025 RPM Bot <rpm-bot@coder966.net> - 11.72.9
- Update to 11.72.9

* Fri Nov 21 2025 RPM Bot <rpm-bot@coder966.net> - 11.72.8
- Update to 11.72.8

* Thu Nov 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.72.5
- Update to 11.72.5

* Wed Nov 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.72.3
- Update to 11.72.3

* Sat Nov 15 2025 RPM Bot <rpm-bot@coder966.net> - 11.71.7
- Update to 11.71.7

* Fri Nov 14 2025 RPM Bot <rpm-bot@coder966.net> - 11.71.5
- Update to 11.71.5

* Fri Nov 07 2025 RPM Bot <rpm-bot@coder966.net> - 11.70.6
- Update to 11.70.6

* Wed Nov 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.70.2
- Update to 11.70.2

* Mon Nov 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.70.0
- Update to 11.70.0

* Fri Oct 31 2025 RPM Bot <rpm-bot@coder966.net> - 11.69.6
- Update to 11.69.6

* Wed Oct 29 2025 RPM Bot <rpm-bot@coder966.net> - 11.69.2
- Update to 11.69.2

* Mon Oct 27 2025 RPM Bot <rpm-bot@coder966.net> - 11.69.0
- Update to 11.69.0

* Fri Oct 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.68.5
- Update to 11.68.5

* Thu Oct 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.68.4
- Update to 11.68.4

* Tue Oct 21 2025 RPM Bot <rpm-bot@coder966.net> - 11.68.0
- Update to 11.68.0

* Fri Oct 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.67.5
- Update to 11.67.5

* Thu Oct 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.67.3
- Update to 11.67.3

* Mon Oct 13 2025 RPM Bot <rpm-bot@coder966.net> - 11.67.0
- Update to 11.67.0

* Fri Oct 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.66.5
- Update to 11.66.5

* Thu Oct 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.66.3
- Update to 11.66.3

* Sat Oct 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.65.4
- Update to 11.65.4

* Thu Oct 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.65.2
- Update to 11.65.2

* Fri Sep 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.64.7
- Update to 11.64.7

* Thu Sep 25 2025 RPM Bot <rpm-bot@coder966.net> - 11.64.6
- Update to 11.64.6

* Wed Sep 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.64.2
- Update to 11.64.2

* Mon Sep 22 2025 RPM Bot <rpm-bot@coder966.net> - 11.64.0
- Update to 11.64.0

* Sat Sep 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.63.6
- Update to 11.63.6

* Fri Sep 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.63.5
- Update to 11.63.5

* Thu Sep 18 2025 RPM Bot <rpm-bot@coder966.net> - 11.63.4
- Update to 11.63.4

* Wed Sep 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.63.3
- Update to 11.63.3

* Tue Sep 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.63.1
- Update to 11.63.1

* Mon Sep 15 2025 RPM Bot <rpm-bot@coder966.net> - 11.63.0
- Update to 11.63.0

* Fri Sep 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.62.7
- Update to 11.62.7

* Thu Sep 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.62.6
- Update to 11.62.6

* Wed Sep 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.62.1
- Update to 11.62.1

* Fri Sep 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.61.8
- Update to 11.61.8

* Thu Sep 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.61.7
- Update to 11.61.7

* Wed Sep 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.61.5
- Update to 11.61.5

* Mon Sep 01 2025 RPM Bot <rpm-bot@coder966.net> - 11.61.0
- Update to 11.61.0

* Fri Aug 29 2025 RPM Bot <rpm-bot@coder966.net> - 11.60.4
- Update to 11.60.4

* Thu Aug 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.60.3
- Update to 11.60.3

* Tue Aug 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.60.1
- Update to 11.60.1

* Fri Aug 22 2025 RPM Bot <rpm-bot@coder966.net> - 11.59.5
- Update to 11.59.5

* Thu Aug 21 2025 RPM Bot <rpm-bot@coder966.net> - 11.59.4
- Update to 11.59.4

* Wed Aug 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.59.3
- Update to 11.59.3

* Tue Aug 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.59.1
- Update to 11.59.1

* Sat Aug 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.58.4
- Update to 11.58.4

* Thu Aug 14 2025 RPM Bot <rpm-bot@coder966.net> - 11.58.3
- Update to 11.58.3

* Wed Aug 13 2025 RPM Bot <rpm-bot@coder966.net> - 11.58.2
- Update to 11.58.2

* Tue Aug 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.58.1
- Update to 11.58.1

* Mon Aug 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.58.0
- Update to 11.58.0

* Fri Aug 08 2025 RPM Bot <rpm-bot@coder966.net> - 11.57.6
- Update to 11.57.6

* Thu Aug 07 2025 RPM Bot <rpm-bot@coder966.net> - 11.57.5
- Update to 11.57.5

* Wed Aug 06 2025 RPM Bot <rpm-bot@coder966.net> - 11.57.1
- Update to 11.57.1

* Mon Aug 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.57.0
- Update to 11.57.0

* Fri Aug 01 2025 RPM Bot <rpm-bot@coder966.net> - 11.56.4
- Update to 11.56.4

* Thu Jul 31 2025 RPM Bot <rpm-bot@coder966.net> - 11.56.3
- Update to 11.56.3

* Fri Jul 25 2025 RPM Bot <rpm-bot@coder966.net> - 11.55.5
- Update to 11.55.5

* Thu Jul 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.55.4
- Update to 11.55.4

* Wed Jul 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.55.3
- Update to 11.55.3

* Tue Jul 22 2025 RPM Bot <rpm-bot@coder966.net> - 
- Update to 

* Mon Jul 21 2025 RPM Bot <rpm-bot@coder966.net> - 11.55.0
- Update to 11.55.0

* Sat Jul 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.54.6
- Update to 11.54.6

* Thu Jul 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.54.3
- Update to 11.54.3

* Tue Jul 15 2025 RPM Bot <rpm-bot@coder966.net> - 11.54.1
- Update to 11.54.1

* Mon Jul 14 2025 RPM Bot <rpm-bot@coder966.net> - 11.54.0
- Update to 11.54.0

* Sat Jul 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.53.5
- Update to 11.53.5

* Fri Jul 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.53.4
- Update to 11.53.4

* Wed Jul 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.53.0
- Update to 11.53.0

* Sat Jul 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.52.5
- Update to 11.52.5

* Fri Jul 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.52.4
- Update to 11.52.4

* Sat Jun 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.51.5
- Update to 11.51.5

* Fri Jun 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.50.5
- Update to 11.50.5

* Thu Jun 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.50.2
- Update to 11.50.2

* Tue Jun 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.50.1
- Update to 11.50.1

* Fri Jun 13 2025 RPM Bot <rpm-bot@coder966.net> - 11.49.4
- Update to 11.49.4

* Wed Jun 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.49.1
- Update to 11.49.1

* Mon Jun 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.49.0
- Update to 11.49.0

* Fri Jun 06 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.5
- Update to 11.48.5

* Thu Jun 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.4
- Update to 11.48.4

* Wed Jun 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.2
- Update to 11.48.2

* Mon Jun 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.0
- Update to 11.48.0

* Fri May 30 2025 RPM Bot <rpm-bot@coder966.net> - 11.47.4
- Update to 11.47.4

* Tue May 27 2025 RPM Bot <rpm-bot@coder966.net> - 11.47.1
- Update to 11.47.1

* Fri May 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.46.6
- Update to 11.46.6

* Tue May 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.46.2
- Update to 11.46.2

* Mon May 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.46.1
- Update to 11.46.1

* Fri May 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.45.6
- Update to 11.45.6

* Thu May 15 2025 RPM Bot <rpm-bot@coder966.net> - 11.45.3
- Update to 11.45.3

* Mon May 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.45.0
- Update to 11.45.0

* Mon May 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.44.0
- Update to 11.44.0

* Fri May 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.43.4
- Update to 11.43.4

* Tue Apr 29 2025 RPM Bot <rpm-bot@coder966.net> - 11.43.2
- Update to 11.43.2

* Sat Apr 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.42.5
- Update to 11.42.5

* Thu Apr 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.42.4
- Update to 11.42.4

* Wed Apr 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.42.3
- Update to 11.42.3

* Thu Apr 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.41.4
- Update to 11.41.4

* Wed Apr 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.41.2
- Update to 11.41.2

* Sat Apr 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.6
- Update to 11.40.6

* Thu Apr 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.4
- Update to 11.40.4

* Tue Apr 08 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.1
- Update to 11.40.1

* Mon Apr 07 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.0
- Update to 11.40.0

* Fri Apr 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.39.5
- Update to 11.39.5

* Wed Apr 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.39.2
- Update to 11.39.2

* Fri Mar 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.38.5
- Update to 11.38.5

* Fri Mar 21 2025 RPM Bot <rpm-bot@coder966.net> - 11.37.5
- Update to 11.37.5

* Thu Mar 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.37.3
- Update to 11.37.3

* Tue Mar 18 2025 RPM Bot <rpm-bot@coder966.net> - 11.37.1
- Update to 11.37.1

* Fri Mar 14 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.6
- Update to 11.36.6

* Thu Mar 13 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.3
- Update to 11.36.3

* Tue Mar 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.1
- Update to 11.36.1

* Mon Mar 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.0
- Update to 11.36.0

* Fri Mar 07 2025 RPM Bot <rpm-bot@coder966.net> - 11.35.4
- Update to 11.35.4

* Wed Mar 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.35.2
- Update to 11.35.2

* Mon Mar 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.35.0
- Update to 11.35.0

* Fri Feb 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.34.5
- Update to 11.34.5

* Thu Feb 27 2025 RPM Bot <rpm-bot@coder966.net> - 11.34.4
- Update to 11.34.4

* Wed Feb 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.34.3
- Update to 11.34.3

* Thu Feb 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.33.4
- Update to 11.33.4

* Mon Feb 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.33.0
- Update to 11.33.0

* Wed Feb 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.32.2
- Update to 11.32.2

* Tue Feb 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.32.1
- Update to 11.32.1

* Mon Feb 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.31.4
- Update to 11.31.4

* Thu Feb 06 2025 RPM Bot <rpm-bot@coder966.net> - 11.31.3
- Update to 11.31.3

* Mon Feb 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.31.0
- Update to 11.31.0

* Fri Jan 31 2025 RPM Bot <rpm-bot@coder966.net> - 11.30.4
- Update to 11.30.4

* Thu Jan 30 2025 RPM Bot <rpm-bot@coder966.net> - 11.30.3
- Update to 11.30.3

* Tue Jan 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.30.1
- Update to 11.30.1

* Fri Jan 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.29.5
- Update to 11.29.5

* Thu Jan 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.29.3
- Update to 11.29.3

* Sat Jan 18 2025 RPM Bot <rpm-bot@coder966.net> - 11.28.4
- Update to 11.28.4

* Thu Jan 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.28.3
- Update to 11.28.3

* Thu Jan 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.27.3
- Update to 11.27.3

* Wed Jan 08 2025 RPM Bot <rpm-bot@coder966.net> - 11.27.1
- Update to 11.27.1

* Thu Dec 19 2024 RPM Bot <rpm-bot@coder966.net> - 11.23.3
- Update to 11.23.3

* Tue Dec 17 2024 RPM Bot <rpm-bot@coder966.net> - 11.23.1
- Update to 11.23.1

* Fri Dec 06 2024 RPM Bot <rpm-bot@coder966.net> - 11.22.0
- Update to 11.22.0

* Tue Nov 26 2024 RPM Bot <rpm-bot@coder966.net> - 11.21.0
- Update to 11.21.0

* Mon Nov 18 2024 RPM Bot <rpm-bot@coder966.net> - 11.20.0
- Update to 11.20.0

* Fri Nov 08 2024 RPM Bot <rpm-bot@coder966.net> - 11.19.0
- Update to 11.19.0

* Wed Oct 23 2024 RPM Bot <rpm-bot@coder966.net> - 11.18.0
- Update to 11.18.0

* Tue Oct 15 2024 RPM Bot <rpm-bot@coder966.net> - 11.17.0
- Update to 11.17.0

* Wed Oct 09 2024 RPM Bot <rpm-bot@coder966.net> - 11.16.0
- Update to 11.16.0

* Tue Oct 01 2024 RPM Bot <rpm-bot@coder966.net> - 11.15.0
- Update to 11.15.0

* Wed Sep 25 2024 RPM Bot <rpm-bot@coder966.net> - 11.14.0
- Update to 11.14.0

* Thu Sep 19 2024 RPM Bot <rpm-bot@coder966.net> - 11.13.0
- Update to 11.13.0

* Wed Sep 11 2024 RPM Bot <rpm-bot@coder966.net> - 11.12.0
- Update to 11.12.0

* Wed Sep 04 2024 RPM Bot <rpm-bot@coder966.net> - 11.11.0
- Update to 11.11.0

* Tue Aug 27 2024 RPM Bot <rpm-bot@coder966.net> - 11.10.0
- Update to 11.10.0

* Fri Aug 23 2024 RPM Bot <rpm-bot@coder966.net> - 11.9.0
- Update to 11.9.0

* Wed Aug 14 2024 RPM Bot <rpm-bot@coder966.net> - 11.8.0
- Update to 11.8.0

* Wed Aug 07 2024 RPM Bot <rpm-bot@coder966.net> - 11.7.0
- Update to 11.7.0

* Wed Jul 31 2024 RPM Bot <rpm-bot@coder966.net> - 11.6.1
- Update to 11.6.1

* Wed Jul 24 2024 RPM Bot <rpm-bot@coder966.net> - 11.5.0
- Update to 11.5.0

* Wed Jul 17 2024 RPM Bot <rpm-bot@coder966.net> - 11.4.0
- Update to 11.4.0

* Fri Jul 12 2024 RPM Bot <rpm-bot@coder966.net> - 11.3.2
- Update to 11.3.2

* Wed Jul 10 2024 RPM Bot <rpm-bot@coder966.net> - 11.3.0
- Update to 11.3.0

* Tue Jun 11 2024 RPM Bot <rpm-bot@coder966.net> - 11.2.0
- Update to 11.2.0

* Wed May 22 2024 RPM Bot <rpm-bot@coder966.net> - 11.1.14
- Update to 11.1.14

* Mon May 13 2024 RPM Bot <rpm-bot@coder966.net> - 11.1.0
- Update to 11.1.0

* Fri May 10 2024 RPM Bot <rpm-bot@coder966.net> - 11.0.12
- Update to 11.0.12

* Tue May 07 2024 RPM Bot <rpm-bot@coder966.net> - 11.0.7
- Update to 11.0.7

* Thu May 02 2024 RPM Bot <rpm-bot@coder966.net> - 11.0.4
- Update to 11.0.4

* Thu Apr 04 2024 RPM Bot <rpm-bot@coder966.net> - 10.24.16
- Update to 10.24.16

* Fri Mar 15 2024 RPM Bot <rpm-bot@coder966.net> - 10.24.3
- Update to 10.24.3

* Mon Mar 11 2024 RPM Bot <rpm-bot@coder966.net> - 10.24.0
- Update to 10.24.0

* Tue Mar 05 2024 RPM Bot <rpm-bot@coder966.net> - 10.23.9
- Update to 10.23.9

* Wed Feb 21 2024 RPM Bot <rpm-bot@coder966.net> - 10.23.5
- Update to 10.23.5

* Mon Feb 12 2024 RPM Bot <rpm-bot@coder966.net> - 10.23.0
- Update to 10.23.0

* Fri Jan 12 2024 RPM Bot <rpm-bot@coder966.net> - 10.22.0
- Update to 10.22.0

* Fri Dec 15 2023 RPM Bot <rpm-bot@coder966.net> - 10.21.0
- Update to 10.21.0

* Thu Nov 09 2023 RPM Bot <rpm-bot@coder966.net> - 10.20.0
- Update to 10.20.0

* Sat Oct 21 2023 RPM Bot <rpm-bot@coder966.net> - 10.19.7
- Update to 10.19.7

* Fri Oct 13 2023 RPM Bot <rpm-bot@coder966.net> - 10.19.0
- Update to 10.19.0

* Tue Oct 03 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.10
- Update to 10.18.10

* Mon Sep 25 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.7
- Update to 10.18.7

* Sat Sep 23 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.6
- Update to 10.18.6

* Wed Sep 20 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.4
- Update to 10.18.4

* Tue Sep 19 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.3
- Update to 10.18.3

* Sat Sep 16 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.2
- Update to 10.18.2

* Fri Sep 15 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.1
- Update to 10.18.1

* Wed Sep 13 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.4
- Update to 10.17.4

* Tue Sep 12 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.0
- Update to 10.18.0

* Fri Aug 25 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.4
- Update to 10.17.4

* Tue Aug 22 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.3
- Update to 10.17.3


* Tue Aug 18 2023 coder966 <coder966@gmail.com> - 10.17.0
- Initial Release
