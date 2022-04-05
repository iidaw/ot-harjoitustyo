from password_generation import PasswordGenerator

generate = PasswordGenerator()
pw = generate.ask_length()
print(f"Generated password: {pw}")