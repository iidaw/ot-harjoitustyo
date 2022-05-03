# Ohelmistotekniikka, harjoitustyö


## Dokumentaatio
[Vaatimusmäärittely](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/iidaw/ot-harjoitustyo/blob/master/password_manager/dokumentaatio/kayttohje.md)

## Release

[Release](https://github.com/iidaw/ot-harjoitustyo/releases/tag/viikko5)


## Asennus
1. Suorita komento: _poetry run invoke build_
2. Asenna riippuvuudet komennolla: _poetry install_
3. Ohjelman käynnistys: _poetry run invoke start_

## Komentorivitoiminnot
Testit komennolla: _poetry run invoke test_

Testikattavuus: _poetry run invoke coverage-report_

Koodin automaattinen formatointi: _poetry run invoke format_

Pylint automaattinen laatutarkistus: _poetry run invoke lint_
