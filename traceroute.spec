Summary:	Traces the route taken by packets over a TCP/IP network.
#Summary(pl):	
Name:		traceroute
Version:	1.4a5
Release:	14
License:	BSD
Group:		Applications/Internet
#Group(pl):	
Source:		ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.Z
Patch0:		traceroute-1.4a5-fix.patch
Patch1:		traceroute-1.4a5-secfix.patch
Patch2:		traceroute-1.4a5-alpha.patch
Patch3:		traceroute-1.4a5-autoroute.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%description -l pl

%prep
%setup -q
%patch0 -p1 -b .fix
%patch1 -p1 -b .secfix
%patch2 -p1 -b .alpha
%patch3 -p1 -b .autoroute

%build

%configure
make 
gzip -9nf traceroute.8 CHANGES FILES README

%install
rm -rf $RPM_BUILD_ROOT
install -d  ${RPM_BUILD_ROOT}{%{_sbindir},%{_mandir}/man8}

install -s traceroute $RPM_BUILD_ROOT%{_sbindir}
install traceroute.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,FILES}.gz
# this is set as 4555 by make install, which I don't really like
%attr(4755,root,bin) %{_sbindir}/traceroute
%attr(644,root,root) %{_mandir}/man8/traceroute.8.gz
