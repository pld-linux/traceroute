Summary:	Traces the route taken by packets over a TCP/IP network
Summary(de):	Verfolgt die Route von Paketen Эber ein TCP/IP-Netzwerk
Summary(es):	EnseЯa la ruta que los paquetes usan a travИs de una red TCP/IP
Summary(fr):	DИtermine le route empruntИe par les paquets sur un rИseau TCP/IP
Summary(pl):	Program do ╤ledzenia trasy pakietСw przez sieФ TCP/IP
Summary(pt_BR):	Mostra a rota que os pacotes usam atravИs de uma rede TCP/IP
Summary(ru):	Показывает трассу, по которой проходят пакеты в TCP/IP сети
Summary(tr):	TCP/IP aПlarЩnda paketlerin rotasЩnЩ izler
Summary(uk):	Показу╓ трасу, якою проходять пакети по TCP/IP мереж╕
Summary(zh_CN):	[о╣мЁ]╪Л╡ИмЬбГа╙м╗б╥╬╤╣д╧╓╬ъ
Name:		traceroute
Version:	1.4a12
Release:	8
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.gz
# Source0-md5:	964d599ef696efccdeebe7721cd4828d
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	76539283b9fcb499ba5121a8a06e9825
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-secfix.patch
Patch2:		%{name}-unaligned.patch
Patch3:		%{name}-autoroute.patch
Patch4:		%{name}-lsrr.patch
Patch5:		%{name}-droproot.patch
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	traceroute-nanog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host. Traceroute displays the
IP number and host name (if possible) of the machines along the route
taken by the packets. Traceroute is used as a network debugging tool.
If you're having network connectivity problems, traceroute will show
you where the trouble is coming from along the route.

%description -l de
Traceroute druckt die Route, die von den Paketen Эber ein TCP/IP
eingeschlagen wird. Die Namen (bzw. die IP-Nummern, wenn keine Namen
verfЭgbar sind) der Maschinen, die beim Routing beteiligt sind,
angefangen vom Rechner, auf dem Tracerout lДuft, bis zum Ziel, werden
ausgedruckt, zusammen mit der Zeit bis zum Erhalt der
'EmpfangsbestДtigung'. Dieses Tool kann bei der Diagnose von
Netzwerkproblemen gute Dienste leisten.

%description -l es
Traceroute imprime la ruta que los paquetes hacen a travИs de una red
TCP/IP. Son impresos los nombres (o nЗmeros de IP si los nombres no
estАn disponibles) de las mАquinas que estАn en ruta en paquetes de la
mАquina traceroute, junto con el tiempo que ha llevado para que la
mАquina reciba el reconocimiento (ack) del paquete. Esta herramienta
puede ser muy Зtil para diagnosticar problemas de red.

%description -l fr
traceroute affiche la route que les paquets prennent avec TCP/IP. Il
affiche les noms (ou les numИros IP si les noms ne sont pas
disponibles) des machines qui routent les paquets de la machine sur
laquelle traceroute s'exИcute jusqu'Ю la machine destination, ainsi
que le temps qu'il a fallu pour recevoir un accusИ reception de cette
machine. Cet outil est trХs pratique pour diagnostiquer les problХmes
rИseau

%description -l pl
traceroute wy╤wietla trasЙ pakietСw do podanego komputera.

%description -l pt_BR
Traceroute imprime a rota que os pacotes fazem atravИs de uma rede
TCP/IP. SЦo impressos os nomes (ou nЗmeros de IP se os nomes nЦo
estiverem disponМveis) das mАquinas que estЦo roteando pacotes da
mАquina traceroute, junto com o tempo que levou para a mАquina receber
o reconhecimento (ack) do pacote. Esta ferramenta pode ser muito Зtil
para diagnosticar problemas de rede.

%description -l ru
Traceroute выводит путь, который пакеты проходят по сети TCP/IP. Имена
(или IP-адреса, если имена недоступны) машин, через которые прошли
пакеты по дороге до точки назначения вместе со временем, которое
потребовалось для получения подтверждения о получении пакета от этих
машин. Эта утилита может быть очень полезна для диагностики сетевых
проблем.

%description -l tr
Traceroute, bir TCP/IP aПЩ boyunca paketlerin izledikleri rotanЩn
dЖkЭmЭnЭ ГЩkarЩr. гalЩЧtЩПЩ makineden hedef makineye kadar olan yol
boyunca paketleri yЖnlendiren her makinenin ismi (ya da IP
numaralarЩ), bu makinelerden alЩndЩ bilgisinin alЩnmasЩna kadar geГen
sЭreyle birlikte listelenir. AП sorunlarЩnЩn belirlenmesinde oldukГa
yardЩmcЩ olabilir.

%description -l ru
Traceroute выводит путь, который пакеты проходят по сети TCP/IP. Имена
(или IP-адреса, если имена недоступны) машин, через которые прошли
пакеты по дороге до точки назначения вместе со временем, которое
потребовалось для получения подтверждения о получении пакета от этих
машин. Эта утилита может быть очень полезна для диагностики сетевых
проблем.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1

%build
%{__autoconf}
cp -f %{_datadir}/automake/install-sh .
cp -f %{_datadir}/automake/config.sub .
CFLAGS="%{rpmcflags} -DHAVE_IFF_LOOPBACK -DUSE_KERNEL_ROUTING_TABLE"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install traceroute $RPM_BUILD_ROOT%{_sbindir}
install traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(4754,root,adm) %{_sbindir}/traceroute
%{_mandir}/man8/*
%lang(pl) %{_mandir}/pl/man8/*
%lang(pt) %{_mandir}/pt/man8/*
