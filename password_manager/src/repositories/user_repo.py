from entities.user import User
from database_connection import get_database_connection



def user_by_row(row):
    return User(row["username"], row["password"] if row else None)


class UserRepo:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista"""

    def __init__(self, connection=get_database_connection()):
        """Luokan konstuktori

        Args:
            connection: Connection-olio tietokantaa varten
        """
        self.connection = connection

    def create_user(self, user: User):
        """Tallentaa käyttäjän tietokantaan

        Args:
            user: Tallennetaan User-oliona

        Returns:
            Tallennettu käyttäjä User-oliona
        """

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO Users (username, password) values (?,?)", [
                       user.username, user.password])
        self.connection.commit()

        return user

    def find_all_users(self):
        """Palauttaa kaikki käyttäjät"""

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        return list(map(user_by_row, rows))

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen mukaan

            Args:
                username: Käyttäjätunnus, jonka mukaan käyttäjä palautetaan

            Returns: Palauttaa User-olion käyttäjästä, jos käyttäjä on tietokannassa
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", [username])

        row = cursor.fetchone()

        return user_by_row(row)


user_repository = UserRepo(get_database_connection())
