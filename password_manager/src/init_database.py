from database_connection import get_database_connection, get_database_connection_test


def drop_tables(connection):
    """Poistaa tietokantataulut.
    Args:
        connection (Connection): tietokantayhteyden Connection-olio.
    """

    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists Users;
    ''')

    cursor.execute('''
        drop table if exists Passwords;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.
    Args:
        connection (Connection): tietokantayhtdyden Connection-olio.
    """

    cursor = connection.cursor()
    cursor.execute('''
        create table Users (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        create table Passwords (
            site text primary key,
            username text,
            password text,
            user integer references users
        );
    ''')

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut.
    """

    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


def init_database_test():
    connection_test = get_database_connection_test()
    drop_tables(connection_test)
    create_tables(connection_test)


if __name__ == "__main__":
    initialize_database()
