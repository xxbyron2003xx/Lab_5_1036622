from calendar import c
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, hmac
import os
import base64

def generate_key(password: str, salt: bytes = None) -> bytes:
    if not salt:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt(message: str, password: str) -> bytes:
    key, salt = generate_key(password)
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return salt + encrypted_message

def decrypt(encrypted_message_with_salt: bytes, password: str) -> str:
    salt, encrypted_message = encrypted_message_with_salt[:16], encrypted_message_with_salt[16:]
    key, _ = generate_key(password, salt)
    cipher = Fernet(key)
    try:
        decrypted_message = cipher.decrypt(encrypted_message)
    except Exception as orr:
        print("Error: Token invalido")
        print(str(orr))
        return None
    return decrypted_message.decode()