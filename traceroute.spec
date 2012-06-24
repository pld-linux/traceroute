Summary:	Traces the route taken by packets over a TCP/IP network
Summary(pl):	Program do �ledzenia trasy pakiet�w przez sie� TCP/IP
Summary(pt_BR):	Mostra a rota que os pacotes usam atrav�s de uma rede TCP/IP
Summary(es):	Ense�a la ruta que los paquetes usan a trav�s de una red TCP/IP
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
traceroute wy�wietla tras� pakiet�w do podanego komputera.

%description -l pt_BR
Traceroute imprime a rota que os pacotes fazem atrav�s de uma rede
TCP/IP. S�o impressos os nomes (ou n�meros de IP se os nomes n�o
estiverem dispon�veis) das m�quinas que est�o roteando pacotes
da m�quina traceroute, junto com o tempo que levou para a m�quina
receber o reconhecimento (ack) do pacote. Esta ferramenta pode ser
muito �til para diagnosticar problemas de rede.

%description -l es
Traceroute imprime la ruta que los paquetes hacen a trav�s de una
red TCP/IP. Son impresos los nombres (o n�meros de IP si los nombres
no est�n disponibles) de las m�quinas que est�n en ruta en paquetes
de la m�quina traceroute, junto con el tiempo que ha llevado para
que la m�quina reciba el reconocimiento (ack) del paquete. Esta
herramienta puede ser muy �til para diagnosticar problemas de red.

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
