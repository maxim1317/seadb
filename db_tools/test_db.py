from pymongo import MongoClient

from utils import *
import random
import datetime as dt
import pprint


DB_NAME = 'seadb'
client = MongoClient()
# db = client.drop_database(DB_NAME)
db = client[DB_NAME]


def fill_logins(db):
    db.logins.drop()
    import hashlib as h
    login_list = [
        {"login": "admin"   , "password": h.md5("admin".encode("utf-8")).hexdigest()    , "role": "admin"  },
        {"login": "oberon"  , "password": h.md5("Worms1317".encode("utf-8")).hexdigest(), "role": "admin"  },
        {"login": "user"    , "password": h.md5("user".encode("utf-8")).hexdigest()     , "role": "user"   },
        {"login": "manager" , "password": h.md5("manager".encode("utf-8")).hexdigest()  , "role": "manager"}
    ]
    coll_from_list(db.logins, login_list)
    return login_list


pp = pprint.PrettyPrinter(indent=4)
fill_logins(db)
# pp.pprint(db.ships.find({"load": 0}))
# pp.pprint(db.anchorages.find({"port_id": dest["_id"]}).limit(1)[0]["_id"])
