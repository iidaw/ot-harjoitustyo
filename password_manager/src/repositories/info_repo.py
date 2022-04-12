
import sqlite3
from entities.save_info import Info

# kesken


class InfoRepo:
    def __init__(self, passwords):
        self.db = sqlite3.connect(passwords)
        self.db.isolation_level = None

        self.passwords = passwords

    def create_pw_table(self):
        self.db.execute("BEGIN")
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS Passwords (id INTEGER PRIMARY KEY, site TEXT, username TEXT, password TEXT)")
        self.db.execute("COMMIT")

    def create_password(self, passwords: Info):
        self.db.execute("BEGIN")
        self.db.execute("INSERT INTO Passwords (site, username, password) VALUES (?,?)", [
                        passwords.site, passwords.username, passwords.password])
        self.db.execute("COMMIT")

        # tähän joku korjaus, että saa ton komennon toimimaan!!

        return passwords

    def find_all_passwords(self):
        self.db.execute("BEGIN")
        all_passwords = self.db.execute("SELECT * FROM Passwords").fetchall()
        self.db.execute("COMMIT")

        return all_passwords

    def find_by_site(self, site):
        self.db.execute("BEGIN")
        password_by_site = self.db.execute(
            "SELECT * FROM Passwords WHERE site = ?", [site]).fetchone()
        self.db.execute("COMMIT")

        return password_by_site

    def delete_table(self):
        self.db.execute("BEGIN")
        self.db.execute("DROP TABLE Passwords")
        self.db.execute("COMMIT")

    def delete_passwords(self):
        self.db.execute("BEGIN")
        self.db.execute("DELETE FROM Passwords")
        self.db.execute("COMMIT")

    # def login(self):
     #   valid = False
      #  users = self.find_all_users()

       # if self.user in users:
        #    if self.password ==


if __name__ == '__main__':
    #info_repo = InfoRepo()
    #info_repo.create_pw_table()
    pass
