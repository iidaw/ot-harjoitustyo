import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

database_filename = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
database_file_path = os.path.join(dirname, '..', 'data', database_filename)
