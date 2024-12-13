import sqlite3
import os
import sys
import time

db_file = os.environ.get('DB_FILE')
if db_file is None:
    sys.exit("DB_FILE environment variable must be set")

connection = sqlite3.connect(db_file)

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.close()
