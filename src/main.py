import logging
import json
from sqlalchemy.orm import Session
from test_db import engine, get_db
from EncryptionSubscriber import EncryptionSub

logging.basicConfig(
    filename= 'app.log',
    level= logging.INFO,
    format = '%(message)s',
)

def log_json(level, message, **kwargs):
    log_entry = {"level":level, "message": message, **kwargs}
    logging.info(json.dumps(log_entry))

def main():
    log_json("info", "Application started")

    db : Session = next(get_db())
    log_json("info", "DB session established")

    db.close()
    log_json("info", "DB session closed")

if __name__ == '__main__':
    main()