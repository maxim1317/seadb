from pymongo import MongoClient

DB_NAME = 'seadb'
client = MongoClient()
# db = client.drop_database(DB_NAME)
db = client[DB_NAME]
print(db.cargo_types.count())
