Summary:	Traces the route taken by packets over a TCP/IP network
Summary(pl):	Program do ¶ledzenia trasy pakietów przez sieæ TCP/IP
Name:		traceroute
Version:	1.4a5
Release:	26
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.Z
Patch0:		%{name}-1.4a5-fix.patch
Patch1:		%{name}-1.4a5-secfix.patch
Patch2:		%{name}-1.4a5-alpha.patch
Patch3:		%{name}-1.4a5-autoroute.patch
Patch4:		%{name}-aliases.patch
Patch5:		%{name}-autoroute2.patch
Patch6:		%{name}-bigpacklen.patch
Patch7:		%{name}-droproot.patch
Patch8:		%{name}-llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.patch
Patch9:		%{name}-lsrr.patch
Patch10:	%{name}-sourceroute.patch
Patch11:	%{name}-unaligned.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host. Traceroute displays the
IP number and host name (if possible) of the machines along the route
taken by the packets. Traceroute is used as a network debugging tool.
If you're having network connectivity problems, traceroute will show
you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network
connectivity problems.

%description -l pl
traceroute wy¶wietla trasê pakietów do podanego komputera.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%configure2_13
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install traceroute $RPM_BUILD_ROOT%{_sbindir}
install traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(4754,root,adm) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
