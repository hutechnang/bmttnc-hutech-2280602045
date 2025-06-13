from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    try:
        with open("server_public_key.pem", "rb") as f:
            server_public_key = serialization.load_pem_public_key(f.read())
    except FileNotFoundError:
        print("Error: server_public_key.pem not found. Please run server.py first.")
        return
    except ValueError as e:
        print(f"Error loading public key: {e}")
        return

    parameters = server_public_key.parameters()

    private_key, public_key = generate_client_key_pair(parameters)

    shared_secret = derive_shared_secret(private_key, server_public_key)

    print(f"Shared Secret: {shared_secret.hex()}")

if __name__ == "__main__":
    main()