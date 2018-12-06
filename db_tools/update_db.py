import time, datetime
from utils import *

DB_NAME = 'seadb'


def get_random_load(size_type):
    import random
    load = random.triangular(
        0,
        db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"],
        db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"] - 100000.0
    )
    return


def update_ship(db):
    ships = list(db.ships.find({}))
    for ship in ships:

    return 0


def update_schedules(db):
    ut = db.util
    finished = list(
        db.schedules.find(
            {
                "estimated_end" : {
                    "$gte": last_upd,
                    "$lt" : time
                }
            }
        )
    )
    started = list(
        db.schedules.find(
            {
                "started" : {
                    "$gte": last_upd,
                    "$lt" : time
                }
            }
        )
    )
    current = db.schedules.find(
        {
            "started"      : {"$lte": time},
            "estimated_end": {"$gte": time}
        }
    ).limit(1)[0]
    return 0


def updater(frequency=30):
    client = MongoClient()
    db = client[DB_NAME]

    while True:
        update_ships(db)
        time.sleep(frequency)

    return 0
