# Password Manager

Käyttäjän on mahdollista pitää kirjaa salasanoista ja käyttäjätunnuksista sovelluksen avulla. Sovelluksella on mahdollista luoda satunnaisia salasanoja käyttäjän määritysten mukaisesti.


## Dokumentaatio
[Vaatimusmäärittely](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/kayttohje.md)

[Testausdokumentti](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/testaus.md)


## Python versiosta
Ohjelmaa on testattu Python-versiolla 3.8


## Release

[Loppupalautus](https://github.com/iidaw/ot-harjoitustyo/releases/tag/loppupalautus)


## Asennus 
1. Asenna riippuvuudet komennolla (password_manager hakemistossa): **poetry install**
2. Suorita komento (alustaa tietokannat): **poetry run invoke build**
3. Ohjelman käynnistys: **poetry run invoke start**

## Komentorivitoiminnot
Testit komennolla: **poetry run invoke test**

Testikattavuus: **poetry run invoke coverage-report**

Koodin automaattinen formatointi: **poetry run invoke format**

Pylint automaattinen laatutarkistus: **poetry run invoke lint**
