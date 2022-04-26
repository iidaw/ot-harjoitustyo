#import sqlite3
from entities.user import User
from database_connection import get_database_connection
#from init_database import init_database


def user_by_row(row):
    return User(row["username"], row["password"] if row else None)


class UserRepo:
    def __init__(self, connection=get_database_connection()):
        self.connection = connection

    def create_user(self, user: User):
        # print(":)") testausta varten
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO Users (username, password) values (?,?)", [
                       user.username, user.password])
        self.connection.commit()

        return user

    def find_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        return list(map(user_by_row, rows))

    def find_by_username(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", [username])

        row = cursor.fetchone()

        return user_by_row(row)

    def delete_users(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Users")
        self.connection.commit()


#user_repository = UserRepo(get_database_connection())
