import os
from pymongo import AsyncMongoClient
from dotenv import load_dotenv
from pymongo.errors import PyMongoError
load_dotenv()

MONGO_URL=  os.getenv("MONGO_URL") #stored in codespace secret
DB_NAME=os.getenv("DB_NAME")       #stored in codespace secret

if not MONGO_URL or not DB_NAME:
    raise RuntimeError("MISSING MONGO_URL OR DB_NAME ENVIRONMENT VARIABLES")
    #already tested with missing url and it gives error in terminal

try:
    client=AsyncMongoClient(MONGO_URL)
    db=client[DB_NAME]
except PyMongoError as e:
    raise RuntimeError(f"MongoDB connection error: {e}")
