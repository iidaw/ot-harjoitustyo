import sqlite3
#from config import DATABASE_FILE_PATH


# testausta varten
def get_database_connection_test():
    connection_test = sqlite3.connect("test.db")
    connection_test.row_factory = sqlite3.Row

    return connection_test


# kirjautumista varten
def get_database_connection():

    connection = sqlite3.connect("users.db")
    connection.row_factory = sqlite3.Row

    return connection


# salasanatietojen tallennusta varten
def get_database_connection_info():

    connection_info = sqlite3.connect("passwords.db")
    connection_info.row_factory = sqlite3.Row

    return connection_info
