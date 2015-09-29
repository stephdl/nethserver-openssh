Name: nethserver-openssh
Summary: sshd daemon configuration
Version: 1.1.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

BuildRequires: nethserver-devtools

Requires: openssh-server
Requires: nethserver-base
AutoReq: no

%description
Configure and manage the sshd daemon

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
( cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT )
rm -f %{name}-%{version}-%{release}-filelist

%{genfilelist} $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Tue Mar 03 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- SSH: locked out of 6.6 beta1 - Bug #3015 [NethServer]
- Base: first configuration wizard - Feature #2957 [NethServer]

* Tue Dec 09 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.8-1.ns6
- ssh access remains public when set to private - Bug #2970 [NethServer]
- Release file and MOTD - Enhancement #2845 [NethServer]
- Drop TCP wrappers hosts.allow hosts.deny templates - Enhancement #2785 [NethServer]

* Tue Oct 28 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.7-1.ns6
- Remote access: web interface error when changing the SSH port - Bug #2847 [NethServer]

* Wed Oct 15 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1.ns6
- Backup config: list only relevant files - Feature #2739

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.5-1.ns6
- Removed fs executable bit from UI language catalogs.

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.4-1.ns6
- Default remote access from public networks - Enhancement #2548 [NethServer]
- SSH: connection keep alive - Enhancement #2147 [NethServer]
- Update all inline help documentation - Task #1780 [NethServer]

* Wed Oct 16 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
- Fix expansion of lokkit template #2205
- SSG daemon should listen on 0.0.0.0 #2138
- Db defaults: remove Runlevels prop #2067

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Rebuild for automatic package handling. #1870
- Restart sshd when changing port. #1862

* Mon Mar 18 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- First release
