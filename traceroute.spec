Summary: Traces the route taken by packets over a TCP/IP network.
Name: traceroute
Version: 1.4a5
Release: 14
Copyright: BSD
Group: Applications/Internet
Source: ftp://ftp.ee.lbl.gov/traceroute-1.4a5.tar.Z
Patch0: traceroute-1.4a5-fix.patch
Patch1: traceroute-1.4a5-secfix.patch
Patch2: traceroute-1.4a5-alpha.patch
Patch3: traceroute-1.4a5-autoroute.patch
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.

%prep
%setup -q
%patch0 -p1 -b .fix
%patch1 -p1 -b .secfix
%patch2 -p1 -b .alpha
%patch3 -p1 -b .autoroute

%build

%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/{sbin,man/man8}

make prefix=${RPM_BUILD_ROOT}%{_prefix} install install-man

{ cd $RPM_BUILD_ROOT
  strip .%{_prefix}/sbin/* || :
}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
# this is set as 4555 by make install, which I don't really like
%attr(4755,root,bin)	%{_prefix}/sbin/traceroute
%{_prefix}/man/man8/traceroute.8
