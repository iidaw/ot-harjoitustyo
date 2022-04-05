import random
import string


class PasswordGenerator:
    def __init__(self):
        self.password = []
        

    def ask_length(self):
        self.password_length = int(input("Enter length (number): "))

        return self.generate_password(self.password_length)
        

    def generate_password(self, length):
        all_char = string.ascii_letters + string.digits + string.punctuation

        # alkuun kaikkia merkkejä vähintään 1
        self.password.append(random.choice(string.ascii_lowercase))
        self.password.append(random.choice(string.ascii_uppercase))
        self.password.append(random.choice(string.digits))
        self.password.append(random.choice(string.punctuation))

        # loput
        for _ in range(1, length - 3):
            if len(self.password) < length:
                self.password.append(random.choice(all_char))

        # viimeistely
        random.shuffle(self.password)
        final_password = "".join(self.password)

        return final_password


if __name__ == "__main__":
    generate = PasswordGenerator()
    pw = generate.ask_length()
    print(f"Generated password: {pw}")
