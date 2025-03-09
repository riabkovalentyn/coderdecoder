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


class EncryptionSub:
    @staticmethod
    def encrypt_sens_fields(mapper, connection, target):
        for field in target.__table__.columns.keys():
            value = getattr(target, field)
            if isinstance(value,str):
                setattr(target, field, encrypt(value))
            log_json("info", "Data encrypted before insert/ubpdate", entity = str(target))

    @staticmethod
    def decrypt_sens_fields(target, context):
        for field in target.__table__.columns.keys():
            value = getattr(target, field)
            if isinstance(value, str):
                setattr(target, field, decryption(value))
            log_json("info", "Data decrypted after select", entity = str(target))

