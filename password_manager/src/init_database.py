from database_connection import get_database_connection, get_database_connection_test


def drop_tables_users(connection):
    # poistaa tietokantataulut
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Users;")
    connection.commit()


def create_tables_users(connection):
    # luo tietokantataulut
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT);")
    connection.commit()


def create_table_info(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE Passwords (id PRIMARY KEY, site TEXT, username TEXT, password TEXT);")
    connection.commit()

    # tähän pitäis kai saada joku mikä yhdistäis tiedot tiettyyn kirjautuneeseen käyttäjään


# testausta varten
def init_database_test():
    connection_test = get_database_connection_test()
    drop_tables_users(connection_test)
    create_tables_users(connection_test)


# oikea
def init_database():
    connection = get_database_connection()
    drop_tables_users(connection)
    create_tables_users(connection)


if __name__ == '__main__':
    init_database()
