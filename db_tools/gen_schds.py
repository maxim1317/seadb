from utils import *
import random
import datetime as dt

schd_sample = {
    "destination_id" : None,
    "pier_id"        : None,
    "started"        : dt.date.today(),
    "estimated_end"  : dt.date.today(),
    "ship_id"        : None,
    "status"         : None
}


def find_estimate(db, ship_id, dest_id, start_time):
    return end_time


def load_unload(db, pier_id, load, start_time):
    rate = db.piers.find({'_id': pier_id}).limit(1)[0]['rate']
    end_time = start_time + dt.timedelta(hours=load / rate)

    return end_time


def voyage_time(ship_speed, distance, start_time):
    end_time = start_time + dt.timedelta(hours=distance / ship_speed)
    return end_time


def gen_stats(db):
    stat_coll = db.statuses
    stat_list = [
        {"status": "FINISHED"   },
        {"status": "PENDING"    },
        {"status": "IN_PROGRESS"},
        {"status": "CANCELED"   },
        {"status": "ЕГГОГ"      },
    ]

    coll_from_list(stat_coll, stat_list)
    return stat_list


def gen_jobs(db):
    job_coll = db.jobs
    job_list = [
        {"job": "VOYAGE"   },
        {"job": "LOADING"  },
        {"job": "UNLOADING"},
    ]

    coll_from_list(job_coll, stat_list)
    return job_list

# { $lookup: {
#   from: <collection to join>,
#   localField: <field from the input documents>,
#   foreignField: <field from the documents of the "from" collection>,
#   as: <output array field>
# } }


def gen_rand_schd(db, amount, ship_id):
    db.fock.drop()
    db.good_ports.drop()
    schd_list = []

    db.fock.drop()
    start_time = dt.datetime.now() - dt.timedelta(weeks=2) - dt.timedelta(days=random.randint(-6, 6))
    ship = db.ships.find({"_id": ship_id}).limit(1)[0]
    ship_type  = ship["ship_type_id"]
    size_type  = ship["size_type_id"]
    ship_speed = ship["avg_speed"]

    db.ports.aggregate([
        {
            '$lookup': {
                'from'        : 'piers'    ,
                'localField'  : '_id'      ,
                'foreignField': 'port_id'  ,
                'as'          : 'port_info'
            }
        },
        {'$out'   : 'fock'}
    ])
    good_ports = list(db.fock.find({'port_info.pier_type': ship_type}))
    coll_from_list(db.good_ports, good_ports)

    load = random.triangular(
        0,
        db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"],
        db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"] - 100000.0
    )

    dep_port   = random.choice(good_ports)["_id"]

    good_piers = list(db.piers.find({'port_id': dep_port, 'pier_type': ship_type}))

    if len(good_piers) <= 1:
        load_pier  = good_piers[0]["_id"]
    else:
        load_pier  = good_piers[random.randint(0, len(good_piers) - 1)]["_id"]

    schd = schd_sample

    end_time = load_unload(db, load_pier, load, start_time)

    schd["destination_id"] = None
    schd["pier_id"]        = load_pier
    schd["started"]        = start_time
    schd["ship_id"]        = ship_id
    schd["estimated_end"]  = end_time
    schd["job"]            = db.jobs.find({"job": "LOADING"}).limit(1)[0]["_id"]
    if start_time > dt.datetime.now():
        schd["status"]     = db.statuses.find({"status": "PENDING"}).limit(1)[0]["_id"]
    elif end_time < dt.datetime.now():
        schd["status"]     = db.statuses.find({"status": "FINISHED"}).limit(1)[0]["_id"]
    else:
        schd["status"]     = db.statuses.find({"status": "IN_PROGRESS"}).limit(1)[0]["_id"]

    db.ships.update_one({'_id': ship_id}, {'$set': {'cargo_amount': load}})
    schd_list.append(schd.copy())

    start_time = end_time
    i = 1
    while i < amount - 1:
        schd = schd_sample

        dests = list(db.destinations.find({'departure': dep_port}))
        if len(list(dests)) == 0:
            # print(dep_port)
            break

        dest = random.choice(dests)

        end_time = voyage_time(ship_speed, dest["distance"], start_time)
        schd["destination_id"] = dest["_id"]
        schd["pier_id"]        = None
        schd["started"]        = start_time
        schd["ship_id"]        = ship_id
        schd["estimated_end"]  = end_time
        schd["job"]            = db.jobs.find({"job": "VOYAGE"}).limit(1)[0]["_id"]
        if start_time > dt.datetime.now():
            schd["status"]     = db.statuses.find({"status": "PENDING"}).limit(1)[0]["_id"]
        elif end_time < dt.datetime.now():
            schd["status"]     = db.statuses.find({"status": "FINISHED"}).limit(1)[0]["_id"]
        else:
            schd["status"]     = db.statuses.find({"status": "IN_PROGRESS"}).limit(1)[0]["_id"]

        dep_port = dest["destination"]
        schd_list.append(schd.copy())

        start_time = end_time

        if (i == amount - 2) and db.good_ports.count_documents({'_id': dep_port}) == 0:
            pass
        else:
            i += 1

    schd = schd_sample

    end_time = load_unload(db, load_pier, load, start_time)

    good_piers = list(db.piers.find({'port_id': dep_port, 'pier_type': ship_type}))

    if len(good_piers) <= 1:
        unload_pier  = good_piers[0]["_id"]
    else:
        unload_pier  = good_piers[random.randint(0, len(good_piers) - 1)]["_id"]

    schd["destination_id"] = None
    schd["pier_id"]        = unload_pier
    schd["started"]        = start_time
    schd["ship_id"]        = ship_id
    schd["estimated_end"]  = end_time
    schd["job"]            = db.jobs.find({"job": "UNLOADING"}).limit(1)[0]["_id"]
    if start_time > dt.datetime.now():
        schd["status"]     = db.statuses.find({"status": "PENDING"}).limit(1)[0]["_id"]
    elif end_time < dt.datetime.now():
        schd["status"]     = db.statuses.find({"status": "FINISHED"}).limit(1)[0]["_id"]
    else:
        schd["status"]     = db.statuses.find({"status": "IN_PROGRESS"}).limit(1)[0]["_id"]

    db.ships.update_one({'_id': ship_id}, {'$set': {'cargo_amount': 0}})
    schd_list.append(schd.copy())

    db.fock.drop()
    db.good_ports.drop()
    coll_from_list(db.schedules, schd_list)
    return schd_list


def gen_schedules(db, per_ship=5):
    from tqdm import tqdm

    db.schedules.drop()

    schd_list = []

    ship_list = list(db.ships.find({}))
    pbar = tqdm(total=len(ship_list) * per_ship, desc="Generating schedules")

    for i in range(len(ship_list)):
        schd = gen_rand_schd(db, amount=per_ship, ship_id=ship_list[i]["_id"])

        pbar.update(per_ship)
        schd_list.extend(schd.copy())

    pbar.close()

    return schd_list
