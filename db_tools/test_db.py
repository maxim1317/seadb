from pymongo import MongoClient

from utils import *
import random
import datetime as dt
import pprint


DB_NAME = 'seadb'
client = MongoClient()
# db = client.drop_database(DB_NAME)
db = client[DB_NAME]


dests = list(db.destinations.find({}))

dest = random.choice(dests)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dest)
pp.pprint(list(db.anchorages.find({"port_id": dest["_id"]}).limit(1)))
# pp.pprint(db.anchorages.find({"port_id": dest["_id"]}).limit(1)[0]["_id"])
