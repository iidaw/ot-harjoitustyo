# Käyttöohje
Lataa projektin viimeinen [release](https://github.com/iidaw/python-password-manager/releases/tag/Loppupalautus).

## Ohjelman käynnistäminen
Asenna riippuvuudet ennen käynnistämistä komennolla (password_manager hakemistossa):
_poetry install_

Alustava ohjelma komennolla:
_poetry run invoke build_

Ohjelman voi käynnistää komennolla:
_poetry run invoke start_


## Ohjelman käyttö
Sovellus aukeaa alkunäkymään, jossa voi valita haluaako kirjautua sisään tai luoda uuden käyttäjätunnuksen.

<img width="499" alt="Näyttökuva 2022-5-11 kello 12 17 39" src="https://user-images.githubusercontent.com/90407612/167816164-dc85b622-b317-4bbb-a23d-6ae340e049ae.png">



### Käyttäjän luominen

Käyttäjän luominen onnistuu create user näkymässä, siihen pääsee painamalla "Create user" painiketta. Siinä syötetään käyttäjän tiedot syötekenttiin ja painetaan "Create" painiketta.
Päänäkymään pääsee takaisin painamalla "Back" painiketta.

<img width="498" alt="Näyttökuva 2022-5-11 kello 12 19 09" src="https://user-images.githubusercontent.com/90407612/167816326-b41e491b-a3a6-4a28-aff7-85ce8ccf3419.png">


### Kirjautuminen

Sisäänkirjautumiseen pääsee painamalla "Login" painiketta. Käyttäjä syöttää tunnuksen ja salasanan syötekenttiin. Painamalla "Login" painiketta pääsee salasanojen tallennusnäkymään.

<img width="500" alt="Näyttökuva 2022-5-11 kello 12 18 28" src="https://user-images.githubusercontent.com/90407612/167816411-181068db-9956-4f4b-9ce7-bc421023dacd.png">


### Salasanatietojen lisääminen

Salasanatietoja saa lisättyä, täyttämällä vaaditut kentät (site, username, password) ja painamalla "Add information" painiketta. Salasanatiedot näkyvät ruudussa, ruutua voi selata ylös/ alas hiirellä. 

Satunnaisen salasanan luomiseen pääsee painamalla "Generate Password" painiketta. 

Ohjelmasta pääsee kirjautumaan ulos painamalla "Log out" painiketta, ohjelma palaa alkunäkymään.

<img width="601" alt="Näyttökuva 2022-5-11 kello 12 20 48" src="https://user-images.githubusercontent.com/90407612/167816952-1ff6bfdc-a9b1-48ad-8a78-003687f184e8.png">


### Salasanan generointi
Klikkaamalla "Generate Password" painiketta, pääsee generoimaan haluamansa pituuden mukaisia salasanoja.

<img width="499" alt="Näyttökuva 2022-5-11 kello 12 21 08" src="https://user-images.githubusercontent.com/90407612/167817167-5e4cbfd1-6f45-4aa4-8dd2-ebd7d0c557c7.png">


### Huomioitavaa käytössä
Tässä mainittuna ohjelmaan jääneet puutteet.

Ohjelma ei tällä hetkellä ilmoita jos on luomassa uutta käyttäjää ja kyseinen käyttäjätunnus onkin jo olemassa (virheilmoitus tulee komentoriville). Ohjelma antaa ilmoituksen, kun käyttäjätunnus on luotu onnistuneesti. Jos ei tule ilmoitusta, käyttäjätunnus on mahdollisesti jo olemassa, siinä tapauksessa yritä luoda käyttäjä toisella tunnuksella.

Ohjelma ei myöskään tällä hetkellä ilmoita, jos yrittää kirjautua sisään käyttäjällä jota ei ole olemassa (virheilmoitus tulee kometoriville). Ohjelma ilmoittaa "Invalid username or password" jos yrittää kirjautua tunnuksella, jolla on väärä salasana. Jos yrittää kirjautua sisälle, eikä se onnistu eikä tule ilmoituksia, ei käyttäjätunnusta ole olemassa.

