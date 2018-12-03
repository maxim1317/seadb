from utils import *
import random
import datetime as dt

schd_sample = {
    "destination_id" : None,
    "pier_id"        : None,
    "started"        : dt.date.today(),
    "estimated_end"  : dt.date.today(),
    "ship_id"        : 0,
    "status"         : "ЕГГОГ"
}


def find_estimate(db, ship_id, dest_id, start_time):
    return end_time


def gen_rand_schd(db, amount, ship_id):
    schd_list = []
    status_list = ["FINISHED", "PENDING", "IN_PROGRESS", "ЕГГОГ", "LOADING", "UNLOADING"]

    dep_port   = db.ports.find({})[random.randint(0, db.ports.count() - 1)]["_id"]
    start_time = dt.date.today() - dt.timedelta(weeks=2) - dt.timedelta(days=random.randint(-6, 6))
    for i in range(1, amount):
        schd = schd_sample

        dest = db.destinations.find({'departure': dep_port})[
            random.randint(0, db.destinations.count_documents({'departure': dep_port}) - 1)
        ]

        schd["destination_id"] = dest["_id"]
        schd["ship_id"]    = ship_id

        dep_port = dest["destination"]
        schd_list.append(schd)

    return schd_list


def gen_schedules(db, max_per_ship=5):
    from tqdm import tqdm

    schd_coll = db.schedules
    schd_list = []

    pbar = tqdm(total=amount, desc="Generating schedules")

    ship_list = list(db.ships.find({}))

    for i in range(len(ship_list)):
        schd = gen_rand_schd(db, amount, ship_list[i]["_id"])

        pbar.update()
        schd_list.extend(schd.copy())

    coll_from_list(schd_coll, schd_list)
    pbar.close()

    return schd_list
