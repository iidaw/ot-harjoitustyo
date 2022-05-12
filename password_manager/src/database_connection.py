import sqlite3
from config import database_file_path


def get_database_connection():
    """Palauttaa yhteyden tietokantaan"""

    connection = sqlite3.connect(database_file_path)
    connection.row_factory = sqlite3.Row

    return connection


# testausta varten
def get_database_connection_test():
    """Palauttaa yhteyden testeissä käytettyyn tietokantaan"""

    connection_test = sqlite3.connect("test.db")
    connection_test.row_factory = sqlite3.Row

    return connection_test
