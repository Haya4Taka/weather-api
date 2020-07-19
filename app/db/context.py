from contextlib import contextmanager
import mysql.connector

from conf.db_conf import DB_CONFIG


@contextmanager
def db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        yield connection
    finally:
        connection.close()
