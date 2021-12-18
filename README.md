# Python-SA-zalbe-na-igrace [Skill Arena] v.1.0

Kratko upustvo o koristenju navedene skripte:
 

Izgled glavne stranice za unos podataka:

![Imgur Image](https://imgur.com/H5RmQq1.jpg)

Parametri su sljedeći:

Nickname: Nick igraca na serveru

Combobox: Mjesto gdje se bira koju kaznu igrac treba dobiti

Vrijeme: Vrijeme na koje se igrac treba kazniti (Banovi su izrazeni u danima, sve ostalo u minutama)

Lokacija: Mjesto gdje je vrijeme prekrseno (Neutral: Mjesto gdje kazne nisu uvecane) (RP zona: Mjesto gdje su kazne x5) (Pijaca/Plaza: Mjesto gdje su kazne x2)

Razlog: Razlog kaznjavanja

NAPOMENA: Vrijeme i razlog pisete normalno, BEZ OBZIRA jel je prekrsio u RP zoni ili na pijaci/plazi, program ce sam dodati razlog i povecati kaznu ovisno o lokaciji.
 



Evo jedan primjer:

Primjer kaznjavanja igraca: Naruto_Minajasi za PG na pijaci/plazi.

![Imgur Image](https://imgur.com/CDFjGta.jpg)

Zapisuje se kao da nije prekrsio da je prekrsio pravilo na pijaci/plazi, jer ce program sam dodati sve potrebno.

Onda ce se sljedece ispisati:

![Imgur Image](https://imgur.com/p2sycL7.jpg)

NAPOMENA JOS JEDNOM: Skripta sama uveca vrijeme i doda razlog prema potrebi.

 

Evo jedan primjer kako izgleda lista sa vise igraca:

![Imgur Image](https://imgur.com/kYGu7zi.jpg)

Za BanAd se ne treba pisati razlog!

Takodjer program ima jos jednu kolonu koja se zove: "WARN".

Program automatski za jailove/disarmove koji su 120 minuta ili veci, ispisuje da ga je potrebno Warnovati.



Instalacija potrebnih modula za ovu skriptu:

Ukucati u cmd.exe

python3 -m pip install --upgrade pip

python3 -m pip install --upgrade Pillow

pip install tk
