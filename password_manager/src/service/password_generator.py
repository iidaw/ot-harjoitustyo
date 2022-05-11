import string
import random


def password_generator(length):
    """Luo satunnaisen salasanan käyttäjän valitsemalla pituudella"""
    password = []
    all_char = string.ascii_letters + string.digits + string.punctuation

    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    for _ in range(1, length - 3):
        if len(password) < length:
            password.append(random.choice(all_char))

    random.shuffle(password)
    final_password = "".join(password)

    return final_password
