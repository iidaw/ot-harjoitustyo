# Password manager

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

[Release viikko 6](https://github.com/iidaw/ot-harjoitustyo/releases/tag/viikko6)


## Asennus 
1. Asenna riippuvuudet komennolla (password_manager hakemistossa): _poetry install_
2. Suorita komento: _poetry run invoke build_
3. Ohjelman käynnistys: _poetry run invoke start_

## Komentorivitoiminnot
Testit komennolla: _poetry run invoke test_

Testikattavuus: _poetry run invoke coverage-report_

Koodin automaattinen formatointi: _poetry run invoke format_

Pylint automaattinen laatutarkistus: _poetry run invoke lint_
