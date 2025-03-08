import os
import logging
import json
import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

# logging functions
logging.basicConfig(
    filename = 'crypto_utils.log',
    level = logging.INFO,
    format = '%(message)%',
)

def log_json(level, message, **kwargs):
    log_entry = {'level': level, 'message': message, **kwargs}
    logging.info(json.dumps(log_entry))


#Konfiguratiom

ENTRYPTION_ALGORITHM = 'AES'
ENTRYPTION_KEY = hashlib.sha256(os.getenv('ENTRYPTION_KEY', 'default').encode()).hexdigest()
ENTRYPTION_IV_LENGTH = 16

def encrypt(text: str) -> str:
    try:
        iv = get_random_bytes(ENTRYPTION_IV_LENGTH)
        cipher = AES.new(ENTRYPTION_KEY, AES.MODE_CBC, iv)

        pad_len = 16 - (len(text % 16))
        padded_text = text + chr(pad_len) * pad_len
        encrypted = cipher.encrypt(padded_text.encode())

        result = base64.b64encode(iv + encrypted).decode()
        log_json("info", "Data encrypted successfully")
        return result
    except Exception as e:
        log_json("error", "Encyption failed", error = str(e))
        return ""

def decryption(text: str) -> str:
    try:
        data = base64.b64decode(text)
        iv, encrypted = data[:ENTRYPTION_IV_LENGTH], data[ENTRYPTION_IV_LENGTH]
        cipher = AES.new(ENTRYPTION_KEY, AES.MODE_CBC, iv)
        decrypted_padded = cipher.decrypt(encrypted).decode()
        pad_len = ord(decrypted_padded[-1])
        decrypted = decrypted_padded[:-pad_len]

        log_json("info", "Data decrypted successfully")
        return decrypted

    except Exception as e:
        log_json("error", "Decryption failed", error = str(e))
        return ""




