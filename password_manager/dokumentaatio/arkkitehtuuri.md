# Arkkitehtuurikuvaus

## Rakenne

<img width="529" alt="Näyttökuva 2022-4-12 kello 20 00 25" src="https://user-images.githubusercontent.com/90407612/163015661-9b7fdaba-c57a-4f74-9ba9-0bbbdd29b8c8.png">

## Päätoiminnallisuudet

### Käyttäjän sisäänkirjautuminen
Sekvenssikaavio käyttäjän sisäänkirjautumisesta:


<img width="609" alt="Näyttökuva 2022-4-26 kello 21 11 48" src="https://user-images.githubusercontent.com/90407612/165364996-aec054e7-8ddd-43f4-ad32-9f53f73ca5a8.png">

Kirjautumisnäkymässä kenttiin kirjoitetaan käyttäjätunnus ja salasana, jonka jälkeen klikataan "Login" painiketta. Painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan Service:n avulla, ja sillä tarkistetaan, onko käyttäjätunnusta ja salasanaa olemassa. Jos käyttäjätunnus ja salasana löytyvät vaihtuu näkymäksi show_add_password_view().

### Uuden käyttäjän luominen

Tapahtumankäsittelijä kutsuu metodia create_user parametrinaan luotavan käyttäjän tunnus ja salasana. Jos käyttäjää ei ole vielä olemassa luodaan sellainen annetuilla tiedoilla luokkien UserRepo ja User avulla. UserRpo luo uuden käyttäjän tallentaen ne User-olion muodossa.

### Salasanatietojen tallennus
Salasananäkymässä kenttiin kirjoitetaan sivusto/ appi ja sillä käyttössä olevat käyttäjätunnus ja salasana, jonka jälkeen painetaan "Add information" painiketta. Painikkeen tapahtumakäsittelijä kutsuu sovelluslogiikan InfoRepo:n avulla. InfoRepo tallentaa uuden salasanatiedon PasswordInfo-olion muodossa.

### Satunnaisen salasanan luominen

Käyttäjä syöttää salasanan halutun pituuden ja salasana luodaan password_generator-metodin avulla, metodi saa attribuutiksi PasswordGeneratorView:n length.entry:lle annetun pituuden.


## Tietojen pysyväistallennus
Luokat InfoRepo ja UserRepo vastaavat tietojen tallennuksesta. Tiedot tallentuvat SQLite-tietokantaan.

Käyttäjät tallennetaan SQL-tietokannan tauluun Users ja käyttäjien tallentamat tiedot tallennetaan SQL-tietokannan tauluun Passwords. Taulut alustetaan init_database.py-tiedostossa.
