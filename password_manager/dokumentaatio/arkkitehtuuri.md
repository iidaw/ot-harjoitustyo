<img width="529" alt="Näyttökuva 2022-4-12 kello 20 00 25" src="https://user-images.githubusercontent.com/90407612/163015661-9b7fdaba-c57a-4f74-9ba9-0bbbdd29b8c8.png">

## Päätoiminnallisuudet
Sekvenssikaavio käyttäjän sisäänkirjautumisesta:
<img width="609" alt="Näyttökuva 2022-4-26 kello 21 11 48" src="https://user-images.githubusercontent.com/90407612/165364996-aec054e7-8ddd-43f4-ad32-9f53f73ca5a8.png">

Kirjautumisnäkymässä kenttiin kirjoitetaan käyttäjätunnus ja salasana, jonka jälkeen klikataan "Login" painiketta. Painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan Service:n avulla, ja sillä tarkistetaan, onko käyttäjätunnusta ja salasanaa olemassa. Jos käyttäjätunnus ja salasana löytyvät vaihtuu näkymäksi show_add_password_view().
