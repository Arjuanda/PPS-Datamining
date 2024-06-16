import secrets

def generate_secret_key():
    return secrets.token_hex(16)

if __name__ == "__main__":
    print("Your Flask secret key is:", generate_secret_key())
