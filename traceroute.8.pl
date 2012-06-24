.\" {PTM/PB/0.2/01-06-1999/"Drukuj tras� pakiet�w"}
.\" Translation (c) 1999 Przemek Borys <pborys@dione.ids.pl>
.\" Copyright (c) 1990, 1991, 1993
.\"	The Regents of the University of California.  All rights reserved.
.\"
.\" This code is derived from software contributed to Berkeley by
.\" Van Jacobson.
.\"
.\" Redistribution and use in source and binary forms, with or without
.\" modification, are permitted provided that the following conditions
.\" are met:
.\" 1. Redistributions of source code must retain the above copyright
.\"    notice, this list of conditions and the following disclaimer.
.\" 2. Redistributions in binary form must reproduce the above copyright
.\"    notice, this list of conditions and the following disclaimer in the
.\"    documentation and/or other materials provided with the distribution.
.\" 3. All advertising materials mentioning features or use of this software
.\"    must display the following acknowledgement:
.\"	This product includes software developed by the University of
.\"	California, Berkeley and its contributors.
.\" 4. Neither the name of the University nor the names of its contributors
.\"    may be used to endorse or promote products derived from this software
.\"    without specific prior written permission.
.\"
.\" THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
.\" ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
.\" IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
.\" ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
.\" FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
.\" DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
.\" OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
.\" HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
.\" LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
.\" OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
.\" SUCH DAMAGE.
.\"
.\"     @(#)traceroute.8	8.1 (Berkeley) 6/6/93
.\"
.Dd 6 Czerwiec, 1993
.Dt TRACEROUTE 8
.Os BSD 4.3
.Sh NAZWA
.Nm traceroute
.Nd drukuj tras�, kt�r� przebiegaj� pakiety do hosta sieciowego
.Sh SK�ADNIA
.Nm traceroute
.Op Fl m Ar max_ttl
.Op Fl n
.Op Fl p Ar port
.Op Fl q Ar nqueries
.Op Fl r
.Bk -words
.Op Fl s Ar src_addr
.Ek
.Op Fl t Ar tos
.Op Fl w Ar waittime
.Ar host
.Op Ar packetsize
.Sh OPIS
Internet jest wielk� i skomplikowan� agregacj� sprz�tu sieciowego,
po��czonego ze sob� poprzez bramki (gateways). �ledzenie trasy, kt�r�
pod��aj� pakiety danej osoby (lub znajdywanie paskudnej bramki, odrzucaj�cej
twoje pakiety) mo�e by� trudne.
.Nm Traceroute
wykorzystuje pole `time to live' protoko�u IP i pr�buje wydoby� odpowied�
.Tn ICMP
.Dv TIME_EXCEEDED
od ka�dej bramki na drodze do okre�lonego hosta.
.Pp
Jedynym wymaganym parametrem jest nazwa hosta docelowego lub jego IP.
Domy�lny pr�bny datagram ma d�ugo�� 38 bajt�w, lecz mo�e to by� zwi�kszone
przez podanie rozmiaru pakietu za nazw� hosta docelowego.
.Pp
Inne opcje to:
.Bl -tag -width Ds
.It Fl m Ar max_ttl
Ustaw maksymalny time-to-live (ttl - `czas �ycia' maksymalna liczba
skok�w - hops) u�ywany w wychodz�cych pakietach pr�bnych. Domy�lnie u�ywa si�
warto�ci 30 (podobnie jak dla po��cze�
.Tn TCP
).
.It Fl n
Drukuj adresy skok�w (hops) numerycznie zamiast symbolicznie i numerycznie
(oszcz�dza szukania w DNS skojarzenia adres-nazwa dla ka�dej napotkanej
po drodze bramki).
.It Fl p Ar port
Ustaw podstawowy numer
.Ar portu
.Tn UDP
u�ywanego w pr�bkach (domy�lnie 33434).
.Nm Traceroute
ma nadziej�, �e nic nie nas�uchuje na portach 
.Tn UDP
od
.Em base
do
.Em base+nhops-1
na ho�cie docelowym (tak, �e zwracany b�dzie komunikat
.Tn ICMP
.Dv PORT_UNREACHABLE
, ko�cz�cy �ledzenie trasy). Je�li co� nas�uchuje na porcie w domy�lnym
zakresie, opcja ta mo�e by� u�yta do wybrania nieu�ywanego zakresu.
.It Fl q Ar nqueries
Ustaw liczb� pr�b na ka�de `ttl' na
.Ar nqueries
(domy�lnie trzy pr�by).
.It Fl r
Obejd� normalne tablice trasowania (routingu) i wysy�aj bezpo�rednio do
hosta w przy��czonej sieci.
Je�li host nie znajduje si� w bezpo�rednio przy��czonej sieci, zwracany jest
b��d.
Opcja ta mo�e by� u�yta do pingowania hosta lokalnego poprzez interfejs,
kt�ry nie ma przez siebie �adnej trasy (route) (np. po porzuceniu interfejsu
przez
.Xr routed 8 ) .
.It Fl s Ar src_addr
U�ywaj zadanego adresu IP (kt�ry musi by� podany jako numer IP, nie
nazwa hosta) jako adresu �r�d�owego w wychodz�cych pakietach pr�bnych. Na
hostach z wi�cej ni� jednym adresem IP, opcja ta mo�e by� u�ywana do
wymuszania adresu �r�d�owego innego ni� adres IP interfejsu, na kt�rym
posy�ana jest pr�bka. Je�li adres IP nie jest jednym z tych adres�w
interfejsowych maszyny, zwracany jest b��d i nic nie jest wysy�ane.
.It Fl t Ar tos
Ustaw
.Em type-of-service
(rodzaj us�ugi) w pakietach pr�bnych na zadan� warto�� (domy�lnie
zero). Warto�� musi by� dziesi�tn� liczb� ca�kowit� z zakresu 0 do 255.
Opcja ta mo�e by� u�ywana do sprawdzania czy r�ne rodzaje us�ug powoduj�
r�ne �cie�ki (je�li nie pracujesz z systemem
.Bx 4.3 Tahoe
lub p�niejszym, mo�e to by� czysto akademickie, poniewa� normalne
us�ugi sieciowe, takie jak telnet i ftp nie pozwol� ci kontrolowa�
.Dv TOS ) .
Nie wszystkie warto�ci
.Dv TOS
s� dozwolone lub maj� znaczenie
\- zobacz specyfikacj� IP. U�ytecznymi warto�ciami s� prawdopodobnie
.Ql \-t 16
(low delay) (ma�e op�nienie) i
.Ql \-t 8
(high throughput) (du�y przep�yw).
.It Fl v
Interaktywne wyj�cie. Listowane s� odebrane pakiety
.Tn ICMP
inne ni�
.Dv TIME_EXCEEDED
i
.Dv UNREACHABLE Ns s .
.It Fl w
Ustaw czas (w sekundach) oczekiwania na odpowied� na pr�bk� (domy�lnie 3
sekundy).
.El
.Pp
Program ten pr�buje �ledzi� tras� pakiet�w IP, kt�r� taki pakiet przeby�by
do danego hosta internetowego. Czyni to odpalaj�c pr�bki
.Tn UDP
z ma�ym ttl (time to live), a nast�pnie nas�uchuj�c od bramki odpowiedzi
.Tn ICMP
"time exceeded". Rozpoczynamy pr�bki z ttl warto�ci jeden i
zwi�kszamy je, a� otrzymamy odpowied�
.Tn ICMP
"port unreachable"
(co znaczy, �e dostali�my si� do "hosta") lub doszli�my do maksimum (co
domy�lnie odpowiada 30 skokom i mo�e by� zmienione flag�
.Fl m
).  Dla ka�dego ttl wysy�ane s� trzy pr�bki (zmieniane flag�
.Fl q
), czego efektem jest wypisanie linijki, pokazuj�cej ttl, adres bramki i
zaokr�glony czas podr�y ka�dej z pr�bek. Je�li odpowiedzi pr�bek przysz�y
z r�nych bramek, wydrukowane zostan� adresy wszystkich odpowiadaj�cych
system�w.
Je�li nie by�o odpowiedzi podczas 3 sekundowego interwa�u (okre�lanego jako
`timeout' i zmienianego flag�
.Fl w
), to dla danej pr�bki drukowane jest "*".
.Pp
Nie chcemy, by docelowy host przetwarza� pr�bki pakiet�w
.Tn UDP
, wi�c docelowy port jest ustawiany na warto�� niespotykan� (je�li
jaki� prostak na ho�cie docelowym u�ywa jednak tej warto�ci, mo�na j� zmieni�
flag�
.Fl p
).
.Pp
Przyk�adem u�ycia i wyj�cia mo�e by�:
.Bd -literal
[yak 71]% traceroute nis.nsf.net.
traceroute to nis.nsf.net (35.1.1.48), 30 hops max, 56 byte packet
1  helios.ee.lbl.gov (128.3.112.1)  19 ms  19 ms  0 ms
2  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  39 ms  19 ms
3  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  39 ms  19 ms
4  ccngw-ner-cc.Berkeley.EDU (128.32.136.23)  39 ms  40 ms  39 ms
5  ccn-nerif22.Berkeley.EDU (128.32.168.22)  39 ms  39 ms  39 ms
6  128.32.197.4 (128.32.197.4)  40 ms  59 ms  59 ms
7  131.119.2.5 (131.119.2.5)  59 ms  59 ms  59 ms
8  129.140.70.13 (129.140.70.13)  99 ms  99 ms  80 ms
9  129.140.71.6 (129.140.71.6)  139 ms  239 ms  319 ms
10  129.140.81.7 (129.140.81.7)  220 ms  199 ms  199 ms
11  nic.merit.edu (35.1.1.48)  239 ms  239 ms  239 ms

.Ed
Zauwa�, �e linie 2 i 3 s� takie same. Sta�o si� to z powodu zapluskwionego
j�dra na systemie odwiedzonym w drugim skoku \- lbl-csam.arpa, kt�re
przekazuje pakiety o zerowym ttl (b��d w rozpowszechnianej wersji
.Tn BSD 4.3
).
Zauwa�, �e musisz zgadywa�, kt�r� konkretnie �cie�k� obieraj� pakiety,
poniewa�
.Tn NSFNet
(129.140)
nie dostarcza translacji adres-na-nazw� dla swoich
.Tn NSS Ns �w .
.Pp
Ciekawszym przyk�adem jest:
.Bd -literal
[yak 72]% traceroute allspice.lcs.mit.edu.
traceroute to allspice.lcs.mit.edu (18.26.0.115), 30 hops max
1  helios.ee.lbl.gov (128.3.112.1)  0 ms  0 ms  0 ms
2  lilac-dmc.Berkeley.EDU (128.32.216.1)  19 ms  19 ms  19 ms
3  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  19 ms  19 ms
4  ccngw-ner-cc.Berkeley.EDU (128.32.136.23)  19 ms  39 ms  39 ms
5  ccn-nerif22.Berkeley.EDU (128.32.168.22)  20 ms  39 ms  39 ms
6  128.32.197.4 (128.32.197.4)  59 ms  119 ms  39 ms
7  131.119.2.5 (131.119.2.5)  59 ms  59 ms  39 ms
8  129.140.70.13 (129.140.70.13)  80 ms  79 ms  99 ms
9  129.140.71.6 (129.140.71.6)  139 ms  139 ms  159 ms
10  129.140.81.7 (129.140.81.7)  199 ms  180 ms  300 ms
11  129.140.72.17 (129.140.72.17)  300 ms  239 ms  239 ms
12  * * *
13  128.121.54.72 (128.121.54.72)  259 ms  499 ms  279 ms
14  * * *
15  * * *
16  * * *
17  * * *
18  ALLSPICE.LCS.MIT.EDU (18.26.0.115)  339 ms  279 ms  279 ms

.Ed
Zauwa�, �e bramki 12, 14, 15, 16 i 17 albo nie przesy�aj� komunikat�w
.Tn ICMP
"time exceeded" lub przesy�aj� je z ttl zbyt ma�ym by nas osi�gn��. 14 \- 17
pracuj� pod kontrol� kodu 
.Tn MIT
C Gateway, kt�ry nie wysy�a "time exceeded"s. B�g jeden wie, co dzieje
si� na 12.
.Pp
Cicha bramka 12 w powy�szym mo�e by� wynikiem b��du w kodzie sieciowym 4.[23]
.Tn BSD
(i jego pochodnych): 4.x (x <= 3) wysy�a nieosi�galne komunikaty, u�ywaj�c
ttl pozosta�ego w oryginalnych datagramach. Zatem, dla bramek, pozosta�y
ttl wynosi zero,
.Tn ICMP
"time exceeded" nie ma szans doj�� z powrotem do nas. Zachowanie tego b��du
jest troch� ciekawsze kiedy pojawi si� na systemie docelowym:
.Bd -literal
1  helios.ee.lbl.gov (128.3.112.1)  0 ms  0 ms  0 ms
2  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  19 ms  39 ms
3  lilac-dmc.Berkeley.EDU (128.32.216.1)  19 ms  39 ms  19 ms
4  ccngw-ner-cc.Berkeley.EDU (128.32.136.23)  39 ms  40 ms  19 ms
5  ccn-nerif35.Berkeley.EDU (128.32.168.35)  39 ms  39 ms  39 ms
6  csgw.Berkeley.EDU (128.32.133.254)  39 ms  59 ms  39 ms
7  * * *
8  * * *
9  * * *
10  * * *
11  * * *
12  * * *
13  rip.Berkeley.EDU (128.32.131.22)  59 ms !  39 ms !  39 ms !

.Ed
Zauwa�, �e jest tu 12 bramek (13 jest ostatecznym celem), a dok�adnie
ostatniej po�owy listy "brakuje". Co naprawd� si� dzieje to to, �e
rip (Sun-3 pracuj�cy pod Sun OS3.5) u�ywa ttl z naszych przychodz�cych
datagram�w jako ttl w swoich odpowiedziach
.Tn ICMP.
Tak wi�c odpowied� nie dojdzie, bo przekroczy zadany czas (timeout) na drodze
powrotnej (bez wysy�ania ostrze�e� do kogokolwiek, bo dla ICMP nie s�
wysy�ane ICMP).
Zmieni si� to, gdy u�yjemy ttl o d�ugo�ci co najmniej dwa razy wi�kszej ni�
d�ugo�� �cie�ki. Np. rip jest w rzeczywisto�ci odleg�y tylko o 7 skok�w.
Odpowied�, kt�ra wraca z ttl o warto�ci 1 jest �ladem, �e
istnieje taki problem. Gdy ttl jest <=1
.Nm Traceroute
za czasem podr�y pakietu drukuje dodatkowo znak
.Sy ! .
Poniewa� dystrybutorzy sprzedaj� sporo oprogramowania przestarza�ego
.Pf ( Tn DEC Ns \'s
Ultrix, Sun 3.x) lub
niestandardowego
.Pq Tn HPUX
, oczekuj �e mo�esz spotka� ten problem cz�sto i uwa�aj, wybieraj�c host
docelowy twoich pr�bek. Innymi mo�liwymi adnotacjami, wyst�puj�cymi po
wydrukowanym czasie, s�
.Sy !H ,
.Sy !N ,
.Sy !P
(otrzyma�em niedost�pno�� hosta, sieci (network) lub protoko�u),
.Sy !S
lub
.Sy !F
(zawiod�a trasa �r�d�a lub niezb�dna jest fragmentacja \- �adne z
tych nie powinno nigdy si� pojawi�). Je�li prawie wszystkie pr�bki dadz�
w wyniku jaki� rodzaj nieosi�galno�ci,
.Nm traceroute
podda si� i wyjdzie.
.Pp
Program ten jest przeznaczony do stosowania w testowaniu, pomiarach i
zarz�dzaniu sieci�. Powinien by� u�ywany g��wnie do r�cznego izolowania
b��d�w.
Nie zaleca si� wykorzystywania traceroute w automatach (skryptach),
gdy� powoduje on du�e obci��enie sieci.
.Sh AUTOR
Zaimplementowane przez Vana Jacobsona wg pomys�u Steve Deering.
Na wyr�nienie zas�uguje Philip Wood, Tim Seaver i Ken Adelman.
.Sh ZOBACZ TAK�E
.Xr netstat 1 ,
.Xr ping 8
.Sh HISTORIA
Komenda
.Nm
jest obecnie w testach.
