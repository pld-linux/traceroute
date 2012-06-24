Summary:	Traces the route taken by packets over a TCP/IP network
Summary(de):	Verfolgt die Route von Paketen �ber ein TCP/IP-Netzwerk
Summary(es):	Ense�a la ruta que los paquetes usan a trav�s de una red TCP/IP
Summary(fr):	D�termine le route emprunt�e par les paquets sur un r�seau TCP/IP
Summary(pl):	Program do �ledzenia trasy pakiet�w przez sie� TCP/IP
Summary(pt_BR):	Mostra a rota que os pacotes usam atrav�s de uma rede TCP/IP
Summary(ru):	���������� ������, �� ������� �������� ������ � TCP/IP ����
Summary(tr):	TCP/IP a�lar�nda paketlerin rotas�n� izler
Summary(uk):	�����դ �����, ���� ��������� ������ �� TCP/IP ����֦
Summary(zh_CN):	[ϵͳ]���������ͨ·���Ĺ���
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
Traceroute druckt die Route, die von den Paketen �ber ein TCP/IP
eingeschlagen wird. Die Namen (bzw. die IP-Nummern, wenn keine Namen
verf�gbar sind) der Maschinen, die beim Routing beteiligt sind,
angefangen vom Rechner, auf dem Tracerout l�uft, bis zum Ziel, werden
ausgedruckt, zusammen mit der Zeit bis zum Erhalt der
'Empfangsbest�tigung'. Dieses Tool kann bei der Diagnose von
Netzwerkproblemen gute Dienste leisten.

%description -l es
Traceroute imprime la ruta que los paquetes hacen a trav�s de una red
TCP/IP. Son impresos los nombres (o n�meros de IP si los nombres no
est�n disponibles) de las m�quinas que est�n en ruta en paquetes de la
m�quina traceroute, junto con el tiempo que ha llevado para que la
m�quina reciba el reconocimiento (ack) del paquete. Esta herramienta
puede ser muy �til para diagnosticar problemas de red.

%description -l fr
traceroute affiche la route que les paquets prennent avec TCP/IP. Il
affiche les noms (ou les num�ros IP si les noms ne sont pas
disponibles) des machines qui routent les paquets de la machine sur
laquelle traceroute s'ex�cute jusqu'� la machine destination, ainsi
que le temps qu'il a fallu pour recevoir un accus� reception de cette
machine. Cet outil est tr�s pratique pour diagnostiquer les probl�mes
r�seau

%description -l pl
traceroute wy�wietla tras� pakiet�w do podanego komputera.

%description -l pt_BR
Traceroute imprime a rota que os pacotes fazem atrav�s de uma rede
TCP/IP. S�o impressos os nomes (ou n�meros de IP se os nomes n�o
estiverem dispon�veis) das m�quinas que est�o roteando pacotes da
m�quina traceroute, junto com o tempo que levou para a m�quina receber
o reconhecimento (ack) do pacote. Esta ferramenta pode ser muito �til
para diagnosticar problemas de rede.

%description -l ru
Traceroute ������� ����, ������� ������ �������� �� ���� TCP/IP. �����
(��� IP-������, ���� ����� ����������) �����, ����� ������� ������
������ �� ������ �� ����� ���������� ������ �� ��������, �������
������������� ��� ��������� ������������� � ��������� ������ �� ����
�����. ��� ������� ����� ���� ����� ������� ��� ����������� �������
�������.

%description -l tr
Traceroute, bir TCP/IP a�� boyunca paketlerin izledikleri rotan�n
d�k�m�n� ��kar�r. �al��t��� makineden hedef makineye kadar olan yol
boyunca paketleri y�nlendiren her makinenin ismi (ya da IP
numaralar�), bu makinelerden al�nd� bilgisinin al�nmas�na kadar ge�en
s�reyle birlikte listelenir. A� sorunlar�n�n belirlenmesinde olduk�a
yard�mc� olabilir.

%description -l ru
Traceroute ������� ����, ������� ������ �������� �� ���� TCP/IP. �����
(��� IP-������, ���� ����� ����������) �����, ����� ������� ������
������ �� ������ �� ����� ���������� ������ �� ��������, �������
������������� ��� ��������� ������������� � ��������� ������ �� ����
�����. ��� ������� ����� ���� ����� ������� ��� ����������� �������
�������.

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
