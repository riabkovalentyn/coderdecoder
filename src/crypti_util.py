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

def encrypt(text: str)
