from entities.save_info import Info
from database_connection import get_database_connection
from entities.user import User

# kesken

# MITEN SAISIN LISÄTTYÄ SEN HETKISEN KÄYTTÄJÄN SALASANATEITOIHIN "USER" KOHTAAN?
# TÄLLÄ HETKELLÄ LISÄÄ SIIHEN "NONE"


def info_by_row(row):
    return Info(row["site"], row["username"], row["password"], row["user"] if row else None)


class InfoRepo:
    """Tallennettuista salasanatiedoista vastaava luokka
    """

    def __init__(self, connection=get_database_connection()):
        self.connection = connection
        self.pw_list = []

    def create_password_info(self, info: Info):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Passwords (site, username, password, user) VALUES (?,?,?,?)", [
                       info.site, info.username, info.password, info.user])

        self.connection.commit()

        # tähän joku korjaus, että saa ton komennon toimimaan!!

        return info

    def find_all_passwords(self):
        """Palauttaa kaikki salasanat

        Returns: Palauttaa listan salasanoja ja niihin liittyviä tietoja
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Passwords")

        passwords = cursor.fetchall()

        return list(map(info_by_row, passwords))

    def find_passwords_by_user(self, user: User):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM Passwords WEHRE (user) = ?", (user.username))
        passwords = cursor.fetchall()

        return list(map(info_by_row, passwords))

    def find_by_site(self, site):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Passwords WHERE site = ?", [site])

        row = cursor.fetchone()

        return info_by_row(row)

    def delete_table(self):
        pass

    def delete_password_info(self):
        """Poistaa valitun salasanan
        """

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Passwords")
        self.connection.commit()


info_repo = InfoRepo(get_database_connection())


if __name__ == '__main__':
    #info_repo = InfoRepo()
    # info_repo.create_pw_table()
    pass

# pitäis kai lisätä vielä jotain
