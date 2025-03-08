from sqlalchemy.event import listeners_for
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative
import json
import logging
from crypto_util import encrypt, decryption


logging.basicConfig(
    filename='encryption_sub.log',
    level= logging.INFO,
    format='%(message)'
)

def log_json(level, message, **kwargs):
    log_entry = {"level": level, "message": message, **kwargs}
    logging.info(json.dumps(log_entry))

Base =  declarative()



