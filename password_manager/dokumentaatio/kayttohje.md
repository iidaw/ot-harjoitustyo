# Käyttöohje
Lataa projektin viimeisimmän releasen lähdekoodi.

## Ohjelman käynnistäminen
Asenna riippuvuudet ennen käynnistämistä komennolla:
_poetry install_

Alustava ohjelma komennolla:
_poetry run invoke build_

Ohjelman voi käynnistää komennolla:
_poetry run invoke start_


## Ohjelman käyttö
Sovellus aukeaa alkunäkymään, jossa voi valita haluaako kirjautua sisään, luoda uuden käyttäjätunnuksen tai generoida salasanan.
Takaisin pääsee aina "Back" painiketta painamalla.

### Käyttäjän luominen

Käyttäjän luominen onnistuu create user näkymässä, siihen pääsee painamalla "Create user" painiketta. Siinä syötetään käyttäjän tiedot syötekenttiin ja painetaan "Create" painiketta.
Päänäkymään pääsee takaisin painamalla "Back" painiketta.

### Kirjautuminen

Sisäänkirjautumiseen pääsee painamalla "Log in" painiketta. Käyttäjä syöttää tunnuksen ja salasanan syötekenttiin. Painamalla "Login" painiketta pääsee salasanojen tallennusnäkymään.
Painamalla "Log out" painiketta, pääsee takaisin päänäkymään ja kirjautuu ulos.

### Salasanan generointi
Klikkaamalla "Generate Password" painiketta, pääsee generoimaan haluamansa pituuden mukaisia salasanoja.
