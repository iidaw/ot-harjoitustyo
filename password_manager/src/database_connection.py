import sqlite3
from config import DATABASE_FILE_PATH

CONNECTION = sqlite3.connect(DATABASE_FILE_PATH)
CONNECTION.row_factory = sqlite3.Row


def get_database_connection():
    """Palauttaa yhteyden tietokantaan
    """
    return CONNECTION


# testausta varten
def get_database_connection_test():
    connection_test = sqlite3.connect("test.db")
    connection_test.row_factory = sqlite3.Row

    return connection_test
