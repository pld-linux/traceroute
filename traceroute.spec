Summary:	Traces the route taken by packets over a TCP/IP network
Summary(de):	Verfolgt die Route von Paketen über ein TCP/IP-Netzwerk
Summary(es):	Enseña la ruta que los paquetes usan a través de una red TCP/IP
Summary(fr):	Détermine le route empruntée par les paquets sur un réseau TCP/IP
Summary(pl):	Program do ¶ledzenia trasy pakietów przez sieæ TCP/IP
Summary(pt_BR):	Mostra a rota que os pacotes usam através de uma rede TCP/IP
Summary(tr):	TCP/IP aðlarýnda paketlerin rotasýný izler
Name:		traceroute
Version:	1.4a12
Release:	3
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.gz
Source1:	%{name}.8.pl
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-secfix.patch
Patch2:		%{name}-unaligned.patch
Patch3:		%{name}-autoroute.patch
Patch4:		%{name}-lsrr.patch
Patch5:		%{name}-droproot.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host. Traceroute displays the
IP number and host name (if possible) of the machines along the route
taken by the packets. Traceroute is used as a network debugging tool.
If you're having network connectivity problems, traceroute will show
you where the trouble is coming from along the route.

%description -l de
Traceroute druckt die Route, die von den Paketen über ein TCP/IP
eingeschlagen wird. Die Namen (bzw. die IP-Nummern, wenn keine Namen
verfügbar sind) der Maschinen, die beim Routing beteiligt sind,
angefangen vom Rechner, auf dem Tracerout läuft, bis zum Ziel, werden
ausgedruckt, zusammen mit der Zeit bis zum Erhalt der
'Empfangsbestätigung'. Dieses Tool kann bei der Diagnose von
Netzwerkproblemen gute Dienste leisten.

%description -l es
Traceroute imprime la ruta que los paquetes hacen a través de una red
TCP/IP. Son impresos los nombres (o números de IP si los nombres no
están disponibles) de las máquinas que están en ruta en paquetes de la
máquina traceroute, junto con el tiempo que ha llevado para que la
máquina reciba el reconocimiento (ack) del paquete. Esta herramienta
puede ser muy útil para diagnosticar problemas de red.

%description -l fr
traceroute affiche la route que les paquets prennent avec TCP/IP. Il
affiche les noms (ou les numéros IP si les noms ne sont pas
disponibles) des machines qui routent les paquets de la machine sur
laquelle traceroute s'exécute jusqu'à la machine destination, ainsi
que le temps qu'il a fallu pour recevoir un accusé reception de cette
machine. Cet outil est très pratique pour diagnostiquer les problèmes
réseau

%description -l pl
traceroute wy¶wietla trasê pakietów do podanego komputera.

%description -l pt_BR
Traceroute imprime a rota que os pacotes fazem através de uma rede
TCP/IP. São impressos os nomes (ou números de IP se os nomes não
estiverem disponíveis) das máquinas que estão roteando pacotes da
máquina traceroute, junto com o tempo que levou para a máquina receber
o reconhecimento (ack) do pacote. Esta ferramenta pode ser muito útil
para diagnosticar problemas de rede.

%description -l tr
Traceroute, bir TCP/IP aðý boyunca paketlerin izledikleri rotanýn
dökümünü çýkarýr. Çalýþtýðý makineden hedef makineye kadar olan yol
boyunca paketleri yönlendiren her makinenin ismi (ya da IP
numaralarý), bu makinelerden alýndý bilgisinin alýnmasýna kadar geçen
süreyle birlikte listelenir. Að sorunlarýnýn belirlenmesinde oldukça
yardýmcý olabilir.

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
CFLAGS="%{rpmcflags} -DHAVE_IFF_LOOPBACK"
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/{,pl/}man8}

install traceroute $RPM_BUILD_ROOT%{_sbindir}
install traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man8

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(4754,root,adm) %{_sbindir}/traceroute
%{_mandir}/man8/traceroute.8*
%lang(pl) %{_mandir}/pl/man8/traceroute.8*
