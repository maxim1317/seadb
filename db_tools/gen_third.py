from utils import *
import random
import datetime as dt

import pprint

schd_sample = {
    "destination_id" : None,
    "pier_id"        : None,
    "anchorage_id"   : None,
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


def rest_time(start_time):
    import random
    end_time = start_time + dt.timedelta(days=round(random.triangular(0, 15, mode=3)))

    return end_time


# { $lookup: {
#   from: <collection to join>,
#   localField: <field from the input documents>,
#   foreignField: <field from the documents of the "from" collection>,
#   as: <output array field>
# } }


def gen_rand_schd(db, amount, ship_id, thread_id, pbar):
    s_time = thread_id

    db["fock" + str(s_time)].drop()
    db["good_ports" + str(s_time)].drop()
    schd_list = []

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
        {'$out'   : 'fock' + str(s_time) }
    ])
    good_ports = list(db["fock" + str(s_time)].find({'port_info.pier_type': ship_type}))
    # print(good_ports)
    coll_from_list(db["good_ports" + str(s_time)], good_ports)

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
    schd["anchorage_id"]   = None
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
        ##################################################
        ############          VOYAGE          ############
        ##################################################
        schd = schd_sample

        dests = list(db.destinations.find({'departure': dep_port}))
        if len(list(dests)) == 0:
            # print(dep_port)
            break

        dest = random.choice(dests)

        end_time = voyage_time(ship_speed, dest["distance"], start_time)
        schd["destination_id"] = dest["_id"]
        schd["pier_id"]        = None
        schd["anchorage_id"]   = None
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

        ##################################################
        ############           REST           ############
        ##################################################

        schd = schd_sample

        end_time = rest_time(start_time)

        schd["destination_id"] = None
        schd["pier_id"]        = None
        schd["anchorage_id"]   = db.anchorages.find({"port_id": dest["destination"]}).limit(1)[0]["_id"]
        schd["started"]        = start_time
        schd["ship_id"]        = ship_id
        schd["estimated_end"]  = end_time
        schd["job"]            = db.jobs.find({"job": "RESTING"}).limit(1)[0]["_id"]
        if start_time > dt.datetime.now():
            schd["status"]     = db.statuses.find({"status": "PENDING"}).limit(1)[0]["_id"]
        elif end_time < dt.datetime.now():
            schd["status"]     = db.statuses.find({"status": "FINISHED"}).limit(1)[0]["_id"]
        else:
            schd["status"]     = db.statuses.find({"status": "IN_PROGRESS"}).limit(1)[0]["_id"]

        schd_list.append(schd.copy())

        start_time = end_time

        if (i == amount - 2) and db["good_ports" + str(s_time)].count_documents({'_id': dep_port}) == 0:
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

    # db.ships.update_one({'_id': ship_id}, {'$set': {'cargo_amount': 0}})
    schd_list.append(schd.copy())

    db["fock" + str(s_time)].drop()
    db["good_ports" + str(s_time)].drop()

    pbar.update()
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(schd_list)
    coll_from_list(db.schedules, schd_list)
    return schd_list


def run_batch(db, amount, ship_list, i, pbar):
    for j in range(len(ship_list) // 8):
        if (i * len(ship_list) + j) >= len(ship_list):
            break
        gen_rand_schd(db, amount=amount, ship_id=ship_list[i * len(ship_list) + j]["_id"], thread_id=i, pbar=pbar)
    return 0


def gen_schedules(db, amount=5):
    from tqdm import tqdm
    from threading import Thread

    db.schedules.drop()
    for i in range(8):
        db["fock" + str(i)].drop()
        db["good_ports" + str(i)].drop()

    schd_list = []

    ship_list = list(db.ships.find({}))
    pbar = tqdm(total=len(ship_list), desc=" Generating schedules")

    threads = []
    for i in range(8):
        # schd = gen_rand_schd(db, amount=amount, ship_id=ship_list[i]["_id"], pbar=pbar)
        t = Thread(
            target=run_batch, args=(db, amount, ship_list, i, pbar)
        )
        threads.append(t)
        t.start()

        # pbar.update(amount)
        # schd_list.extend(schd.copy())

    for thread in threads:
        thread.join()

    pbar.close()

    return schd_list
