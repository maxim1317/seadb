from pymongo import MongoClient

from utils import *
import random
import datetime as dt
import pprint


DB_NAME = 'seadb'
client = MongoClient()
# db = client.drop_database(DB_NAME)
db = client[DB_NAME]


def fill_ship_loads(db):
    unfinished_trips = list(db.schedules.find({"estimated_end": {"$gte": dt.datetime.now()}, "pier_id": {"$ne": None}}))
    return unfinished_trips


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fill_ship_loads(db))
# pp.pprint(db.anchorages.find({"port_id": dest["_id"]}).limit(1)[0]["_id"])
