from entities.save_password_info import PasswordInfo
from database_connection import get_database_connection


def info_by_row(row):
    return PasswordInfo(row["site"], row["username"], row["password"], row["user"] if row else None)


class InfoRepo:
    """Tallennettuista salasanatiedoista vastaava luokka
    """

    def __init__(self, connection=get_database_connection()):
        """Luokan konstruktori

            Args:
                connection: Connection-olio tietokantaa varten
        """

        self.connection = connection

    def add_password_info(self, info: PasswordInfo):
        """Lisää tallennettavan salasanan ja siihen liittyvät tiedot

            Args:
                info: taallennettavat salasanatiedot PassworInfo-oliona

            Returns: Palauttaa tallennetun salasanan ja siihen liittyvät tiedot
        """

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Passwords (site, username, password, user) VALUES (?,?,?,?)", [
                       info.site, info.username, info.password, info.user])

        self.connection.commit()

        return info

    def find_passwords_by_user(self, user):
        """Palauttaa kirjautuneen käyttäjän tallentamat salasantiedot

            Args:
                user: kirjautuneen käyttäjän tunnus

            Returns: Palauttaa listan käyttäjän tallentamista salasanoista
        """

        pw_list = []

        cursor = self.connection.cursor()
        passwords = cursor.execute(
            "SELECT * FROM Passwords WHERE user = ?", [user])
        rows = passwords.fetchall()

        for row in rows:
            pw_list.append(info_by_row(row))

        return pw_list


    def delete_password_info(self):
         """Poistaa kaikki salasanat tietokannasta
         """

         cursor = self.connection.cursor()
         cursor.execute("DELETE FROM Passwords")
         self.connection.commit()


info_repo = InfoRepo(get_database_connection())
