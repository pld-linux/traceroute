Summary:	Traces the route taken by packets over a TCP/IP network
Summary(pl):	Program do ¶ledzenia trasy pakietów przez sieæ TCP/IP
Summary(pt_BR):	Mostra a rota que os pacotes usam através de uma rede TCP/IP
Summary(es):	Enseña la ruta que los paquetes usan a través de una red TCP/IP
Name:		traceroute
Version:	1.4a12
Release:	1
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.gz
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-secfix.patch
Patch2:		%{name}-unaligned.patch
Patch3:		%{name}-autoroute.patch
Patch4:		%{name}-lsrr.patch
#Patch5:	%{name}-droproot.patch
BuildRequires:	autoconf
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

%description -l pt_BR
Traceroute imprime a rota que os pacotes fazem através de uma rede
TCP/IP. São impressos os nomes (ou números de IP se os nomes não
estiverem disponíveis) das máquinas que estão roteando pacotes
da máquina traceroute, junto com o tempo que levou para a máquina
receber o reconhecimento (ack) do pacote. Esta ferramenta pode ser
muito útil para diagnosticar problemas de rede.

%description -l es
Traceroute imprime la ruta que los paquetes hacen a través de una
red TCP/IP. Son impresos los nombres (o números de IP si los nombres
no están disponibles) de las máquinas que están en ruta en paquetes
de la máquina traceroute, junto con el tiempo que ha llevado para
que la máquina reciba el reconocimiento (ack) del paquete. Esta
herramienta puede ser muy útil para diagnosticar problemas de red.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1

%build
autoconf
%configure
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
%doc *.gz
%attr(4754,root,adm) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
