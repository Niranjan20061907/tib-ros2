from cryptography.fernet import Fernet

# In a real ROV this key would be:
# - Stored in secure hardware (TPM chip)
# - Loaded from environment variables
# - Never hardcoded like this
# For learning purposes we hardcode it here
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_depth(depth: float) -> str:
    """
    Encrypt a depth reading before sending over ROS 2 topic
    
    COA concept: This uses AES-128 symmetric encryption
    under the hood — fast enough for real-time sensor data
    """
    # Convert float to bytes, then encrypt
    depth_bytes = str(depth).encode('utf-8')
    encrypted = cipher.encrypt(depth_bytes)
    return encrypted.decode('utf-8')

def decrypt_depth(encrypted_str: str) -> float:
    """
    Decrypt a depth reading received from ROS 2 topic
    
    Security concept: Only nodes with the same KEY
    can decrypt — unauthorized nodes see gibberish
    """
    encrypted_bytes = encrypted_str.encode('utf-8')
    decrypted = cipher.decrypt(encrypted_bytes)
    return float(decrypted.decode('utf-8'))