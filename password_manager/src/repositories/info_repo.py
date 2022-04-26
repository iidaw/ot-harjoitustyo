from entities.save_info import Info
from database_connection import get_database_connection_info

# kesken


def info_by_row(row):
    return Info(row["site"], row["username"], row["password"] if row else None)


class InfoRepo:
    def __init__(self, connection=get_database_connection_info()):
        self.connection = connection

    def create_password_info(self, info: Info):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Passwords (site, username, password) VALUES (?,?)", [
                       info.site, info.username, info.password])

        self.connection.commit()

        # tähän joku korjaus, että saa ton komennon toimimaan!!

        return info

    def find_all_passwords(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Passwords")
        rows = cursor.fetchall()

        return list(map(info_by_row, rows))

    def find_by_site(self, site):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Passwords WHERE site = ?", [site])

        row = cursor.fetchone()

        return info_by_row(row)

    def delete_table(self):
        pass

    def delete_password_info(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Passwords")
        self.connection.commit()


if __name__ == '__main__':
    #info_repo = InfoRepo()
    # info_repo.create_pw_table()
    pass

# pitäis kai lisätä vielä jotain
