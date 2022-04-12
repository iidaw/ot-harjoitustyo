from database_connection import get_database_connection, get_database_connection_test


def drop_tables(connection):
    # poistaa tietokantataulut
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Users;")
    connection.commit()


def create_tables(connection):
    # luo tietokantataulut
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT);")
    connection.commit()


# testausta varten
def init_database_test():
    connection_test = get_database_connection_test()
    drop_tables(connection_test)
    create_tables(connection_test)


# oikea
def init_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    init_database()
