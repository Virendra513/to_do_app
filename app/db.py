from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongo_db_url=os.getenv("uri")

client = MongoClient(mongo_db_url)

db=client["items_db"]
collections={"items":db["items"]}
print("MONGODB_URL =", os.getenv("uri"))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
