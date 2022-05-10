from entities.save_info import Info
from database_connection import get_database_connection
from entities.user import User
from service.service import service

# kesken


def info_by_row(row):
    return Info(row["site"], row["username"], row["password"], row["user"] if row else None)


class InfoRepo:
    """Tallennettuista salasanatiedoista vastaava luokka
    """

    def __init__(self, connection=get_database_connection()):
        self.connection = connection

    def create_password_info(self, info: Info):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Passwords (site, username, password, user) VALUES (?,?,?,?)", [
                       info.site, info.username, info.password, info.user])

        self.connection.commit()


        return info

    def find_all_passwords(self):
        """Palauttaa kaikki salasanat

        Returns: Palauttaa listan salasanoja ja niihin liittyviä tietoja
        """

        pw_list = []

        cursor = self.connection.cursor()
        passwords = cursor.execute("SELECT * FROM Passwords")

        rows = passwords.fetchall()

        for row in rows:
            pw_list.append(info_by_row(row))

        #print(rows)

        #return list(map(info_by_row, passwords))
        return pw_list


    def find_passwords_by_user(self, user):
        pw_list = []

        cursor = self.connection.cursor()
        passwords = cursor.execute(
            "SELECT * FROM Passwords WHERE user = ?", [user])
        rows = passwords.fetchall()

        for row in rows:
            pw_list.append(info_by_row(row))

        #return list(map(info_by_row, passwords))


        return pw_list

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
