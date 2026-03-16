from cryptography.fernet import Fernet

# Fixed key — both nodes load the same key
# In production this would be loaded from a secure
# environment variable or hardware security module
KEY = b'A8M3Kp2vX9nL5qR7tY1wZ6jB4cD0eF-hI_uJ3kN='

# Pad to valid Fernet key length
import base64
KEY = base64.urlsafe_b64encode(b'TiburonROVSecretKey2024!!1234567')
cipher = Fernet(KEY)

def encrypt_depth(depth: float) -> str:
    """Encrypt depth reading using AES-128"""
    depth_bytes = str(depth).encode('utf-8')
    encrypted = cipher.encrypt(depth_bytes)
    return encrypted.decode('utf-8')

def decrypt_depth(encrypted_str: str) -> float:
    """Decrypt depth reading using AES-128"""
    encrypted_bytes = encrypted_str.encode('utf-8')
    decrypted = cipher.decrypt(encrypted_bytes)
    return float(decrypted.decode('utf-8'))