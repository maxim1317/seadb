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
    last_upd = db.util.find({}).limit(1)[0]

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

    for s in started:
        db.schedules.update_one({"_id": s["_id"]}, {"$set": {"status" : db.statuses.find({"status": "IN_PROGRESS"}).limit(1)[0]["_id"]}})
        cur_job = db.jobs.find("_id": s["job"]).limit(1)[0]["job"]
        if cur_job == "UNLOADING":
            db.ships.update_one({"_id": s["ship_id"]}, {"$set": {"cargo_amount": get_random_load()}})
    for f in finished:
        db.schedules.update_one({"_id": f["_id"]}, {"$set": {"status" : db.statuses.find({"status": "FINISHED"}).limit(1)[0]["_id"]}})
    return 0


def updater(frequency=30):
    client = MongoClient()
    db = client[DB_NAME]

    while True:
        update_ships(db)
        time.sleep(frequency)

    return 0
