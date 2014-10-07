Summary:	Utilities for mounting and managing CIFS mounts
Name:		cifs-utils
Version:	6.4
Release:	1
License:	GPL v3+
Group:		Daemons
Source0:	ftp://ftp.samba.org/pub/linux-cifs/cifs-utils/%{name}-%{version}.tar.bz2
# Source0-md5:	b7d75b67fd3987952896d27256c7293d
URL:		http://linux-cifs.samba.org/cifs-utils/
BuildRequires:	keyutils-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	talloc-devel
BuildRequires:  pam-devel
Requires:	keyutils
Suggests:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SMB/CIFS protocol is a standard file sharing protocol widely
deployed on Microsoft Windows machines. This package contains tools
for mounting shares on Linux using the SMB/CIFS protocol. The tools in
this package work in conjunction with support in the kernel to allow
one to mount a SMB/CIFS share onto a client and use it as if it were a
standard Linux file system.

%prep
%setup -q

%build
ROOTSBINDIR=%{_sbindir} \
%configure \
	--enable-systemd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/cifscreds
%attr(755,root,root) %{_bindir}/getcifsacl
%attr(755,root,root) %{_bindir}/setcifsacl
%attr(755,root,root) %{_sbindir}/cifs.idmap
%attr(755,root,root) %{_sbindir}/mount.cifs

%attr(755,root,root) %{_libdir}/security/pam_cifscreds.so

%dir %{_libdir}/cifs-utils
%attr(755,root,root) %{_libdir}/cifs-utils/idmapwb.so

%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

