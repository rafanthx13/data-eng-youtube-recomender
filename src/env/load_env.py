import os
from dotenv import load_dotenv

load_dotenv() # Load from './.env'; Nao se usa aspas no '.env' para especificar string

TEST_ENV = os.getenv('DB_HOST') # Retorna None se nao encontrar

if(TEST_ENV == None):
    raise Exception('ENV Variables NOT FOUND')

DB_HOST    = os.getenv('DB_HOST')
DB_USER    = os.getenv('DB_USER')
DB_PORT    = int(os.getenv('DB_PORT'))
DB_PASS    = os.getenv('DB_PASS')
DB_NAME    = os.getenv('DB_NAME')
DB_TABLE   = os.getenv('DB_TABLE')