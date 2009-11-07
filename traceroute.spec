Summary:	Traces the route taken by packets over a TCP/IP network
Summary(de.UTF-8):	Verfolgt die Route von Paketen über ein TCP/IP-Netzwerk
Summary(es.UTF-8):	Enseña la ruta que los paquetes usan a través de una red TCP/IP
Summary(fr.UTF-8):	Détermine le route empruntée par les paquets sur un réseau TCP/IP
Summary(pl.UTF-8):	Program do śledzenia trasy pakietów przez sieć TCP/IP
Summary(pt_BR.UTF-8):	Mostra a rota que os pacotes usam através de uma rede TCP/IP
Summary(ru.UTF-8):	Показывает трассу, по которой проходят пакеты в TCP/IP сети
Summary(tr.UTF-8):	TCP/IP ağlarında paketlerin rotasını izler
Summary(uk.UTF-8):	Показує трасу, якою проходять пакети по TCP/IP мережі
Summary(zh_CN.UTF-8):	[系统]检查网络联通路径的工具
Name:		traceroute
Version:	2.0.13
Release:	1
License:	BSD
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/traceroute/%{name}-%{version}.tar.gz
# Source0-md5:	cbba62e18384c5ed9ad6997dbd7caca9
Patch0:		%{name}-AI_IDN.patch
URL:		http://traceroute.sourceforge.net/
BuildRequires:	rpm >= 4.4.9-56
Obsoletes:	traceroute-nanog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host. Traceroute displays the
IP number and host name (if possible) of the machines along the route
taken by the packets. Traceroute is used as a network debugging tool.
If you're having network connectivity problems, traceroute will show
you where the trouble is coming from along the route.

%description -l de.UTF-8
Traceroute druckt die Route, die von den Paketen über ein TCP/IP
eingeschlagen wird. Die Namen (bzw. die IP-Nummern, wenn keine Namen
verfügbar sind) der Maschinen, die beim Routing beteiligt sind,
angefangen vom Rechner, auf dem Tracerout läuft, bis zum Ziel, werden
ausgedruckt, zusammen mit der Zeit bis zum Erhalt der
'Empfangsbestätigung'. Dieses Tool kann bei der Diagnose von
Netzwerkproblemen gute Dienste leisten.

%description -l es.UTF-8
Traceroute imprime la ruta que los paquetes hacen a través de una red
TCP/IP. Son impresos los nombres (o números de IP si los nombres no
están disponibles) de las máquinas que están en ruta en paquetes de la
máquina traceroute, junto con el tiempo que ha llevado para que la
máquina reciba el reconocimiento (ack) del paquete. Esta herramienta
puede ser muy útil para diagnosticar problemas de red.

%description -l fr.UTF-8
traceroute affiche la route que les paquets prennent avec TCP/IP. Il
affiche les noms (ou les numéros IP si les noms ne sont pas
disponibles) des machines qui routent les paquets de la machine sur
laquelle traceroute s'exécute jusqu'à la machine destination, ainsi
que le temps qu'il a fallu pour recevoir un accusé reception de cette
machine. Cet outil est très pratique pour diagnostiquer les problèmes
réseau

%description -l pl.UTF-8
traceroute wyświetla trasę pakietów do podanego komputera.

%description -l pt_BR.UTF-8
Traceroute imprime a rota que os pacotes fazem através de uma rede
TCP/IP. São impressos os nomes (ou números de IP se os nomes não
estiverem disponíveis) das máquinas que estão roteando pacotes da
máquina traceroute, junto com o tempo que levou para a máquina receber
o reconhecimento (ack) do pacote. Esta ferramenta pode ser muito útil
para diagnosticar problemas de rede.

%description -l ru.UTF-8
Traceroute выводит путь, который пакеты проходят по сети TCP/IP. Имена
(или IP-адреса, если имена недоступны) машин, через которые прошли
пакеты по дороге до точки назначения вместе со временем, которое
потребовалось для получения подтверждения о получении пакета от этих
машин. Эта утилита может быть очень полезна для диагностики сетевых
проблем.

%description -l tr.UTF-8
Traceroute, bir TCP/IP ağı boyunca paketlerin izledikleri rotanın
dökümünü çıkarır. Çalıştığı makineden hedef makineye kadar olan yol
boyunca paketleri yönlendiren her makinenin ismi (ya da IP
numaraları), bu makinelerden alındı bilgisinin alınmasına kadar geçen
süreyle birlikte listelenir. Ağ sorunlarının belirlenmesinde oldukça
yardımcı olabilir.

%description -l ru.UTF-8
Traceroute выводит путь, который пакеты проходят по сети TCP/IP. Имена
(или IP-адреса, если имена недоступны) машин, через которые прошли
пакеты по дороге до точки назначения вместе со временем, которое
потребовалось для получения подтверждения о получении пакета от этих
машин. Эта утилита может быть очень полезна для диагностики сетевых
проблем.

%prep
%setup -q
%if "%{pld_release}" == "ac"
%patch0 -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcflags} -D_GNU_SOURCE=1" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install traceroute/traceroute $RPM_BUILD_ROOT%{_bindir}
ln -s traceroute $RPM_BUILD_ROOT%{_bindir}/traceroute6
ln -s traceroute $RPM_BUILD_ROOT%{_bindir}/tracert

cp -a */*.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo ".so traceroute.8" > $RPM_BUILD_ROOT%{_mandir}/man8/traceroute6.8
echo ".so traceroute.8" > $RPM_BUILD_ROOT%{_mandir}/man8/tracert.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README TODO
%attr(4754,root,adm) %{_bindir}/traceroute
%attr(755,root,root) %{_bindir}/traceroute6
%attr(755,root,root) %{_bindir}/tracert
%{_mandir}/man8/traceroute.8*
%{_mandir}/man8/traceroute6.8*
%{_mandir}/man8/tracert.8*
