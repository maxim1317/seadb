from pymongo import MongoClient, errors
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import re

DB_NAME = 'seadb'


def get_ship_list(auth):
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    ship_list = []
    all_ships = list(db.ships.find({}))

    for ship in all_ships:
        ship_list.append(ship["name"])

    client.close()
    return ship_list


def get_port_list(auth):
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    port_list = []
    all_ports = list(db.ports.find({}))

    for port in all_ports:
        port_list.append(port["name"])

    client.close()
    return port_list


def get_login_list(auth):
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    login_list = []
    all_logins = list(db.logins.find({}))

    for login in all_logins:
        login_list.append(login["login"])

    return login_list


def get_good_ports(auth, pier_type):
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    good_piers = list(db.piers.find({"pier_type": pier_type}))

    good_piers_ids = [i["port_id"] for i in good_piers]

    good_ports = list(db.ports.find({"_id": {"$in": good_piers_ids}}))

    return good_ports


def try_login(login, password):
    try:
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]
        try:
            db.countries.find_one({})
            # print(db.countries.find_one({}))
            return 1
        except errors.OperationFailure:
            print("Authentication failed")
            return 0
    except (errors.OperationFailure, errors.ConfigurationError, errors.InvalidURI):
            print("Authentication failed")
            return 0


# def get_top_10_dict(auth):
#     login, password = auth
#     client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
#     db = client[DB_NAME]

#     return top_10


# def get_top_10_items(auth):
#     login, password = auth
#     client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
#     top_10_items = []

#     return top_10_items

def get_top_10(auth):
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    top_10 = []

    week_list = list(db.week_ports_load.find({}).sort([("amount", -1), ("name", 1)]).limit(10))

    for i in range(0, 10):
        top_10.append({
            "name"  : week_list[i]["name"],
            "amount": str(week_list[i]["amount"])
        })

    return top_10


def get_vessel_info(auth, name):
    import datetime as dt
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    ship = db.ships.find_one({"name": name})

    date = dt.datetime.now()

    cur_task = db.schedules.find_one({
        "$and": [
            {"ship_id"        : ship["_id"]},
            {"started"        : {"$lte": date}},
            {"estimated_end"  : {"$gte": date}},
        ]
    })
    if cur_task is None:
        status = "RESTING"
        load  = "0"
    else:
        status = db.jobs.find_one({"_id": cur_task["job"]})["job"]
        load   = str(int(ship["cargo_amount"]))

    info = {
        "_id"          : ship['_id'],
        "name"         : name,
        "avg_speed"    : str(int(ship["avg_speed"])),
        "home_port"    : db.ports.find_one({"_id": ship["home_port_id"]})["name"],
        "load"         : load,
        "flag"         : db.countries.find_one({"_id": ship["flag_id"]})["name"],
        "class"        : db.sizes.find_one({"_id": ship["size_type_id"]})["name"],
        "cargo_type"   : db.cargo_types.find_one({"_id": ship["ship_type_id"]})["type"],
        "status"       : status,
        "schedule"     : list(db.schedules.find({"ship_id": ship["_id"]}))
    }

    return info


def get_port_info(auth, name):
    import datetime as dt
    from bson import ObjectId

    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    port = db.ports.find_one({"name": name})

    date = dt.datetime.now().date()
    # print(port)

    journal = list(db.port_journals.find({"port_id": port["_id"]}))

    def form_piers():
        container = ObjectId('5c094ca3af5b83063185f786')
        liquid    = ObjectId('5c094ca3af5b83063185f787')
        bulk      = ObjectId('5c094ca3af5b83063185f788')
        bp        = db.piers.count_documents({"port_id": port["_id"], "pier_type": bulk})
        lp        = db.piers.count_documents({"port_id": port["_id"], "pier_type": liquid})
        cp        = db.piers.count_documents({"port_id": port["_id"], "pier_type": container})

        pier_str = \
            "Bulk x" + str(bp) + "\n" + \
            "Liquid x" + str(lp) + "\n" + \
            "Container x" + str(cp)
        return pier_str

    def form_ship_count():
        count = 0
        # print(journal)
        for j in journal:
            if j["date"].date() == date:
                count += 1
        return count

    def form_turnover():
        turnover  = 0

        _date = dt.datetime.now()
        week = _date - dt.timedelta(weeks=1)

        loading   = ObjectId('5c094ca3af5b83063185f78b')
        unloading = ObjectId('5c094ca3af5b83063185f78c')
        _id       = port["_id"]
        listing   = list(
            db.port_journals.find({
                "port_id"  : _id,
                "operation": {
                    "$in"  : [loading, unloading]
                },
                "date"     : {
                    "$gte" : week,
                    "$lt"  : _date,
                }
            })
        )

        ship_ids = []

        for l in listing:
            ship_ids.append(l["ship_id"])

        ship_ids = list(set(ship_ids))

        ships = db.ships.find({"_id": {"$in": ship_ids}})

        for ship in ships:
            turnover += (ship["cargo_amount"])

        return int(turnover / 7.33)

    info = {
        "_id"          : port['_id'],
        "name"         : name,
        "country"      : db.countries.find_one({"_id": port["country_id"]})["name"],
        "location"     : port['location'],
        "piers"        : form_piers(),
        "turnover"     : form_turnover(),
        "ships_in_port": form_ship_count(),
        "journal"      : list(db.port_journals.find({"port_id": port["_id"]}))
    }

    return info


def center(wid):
    from PyQt5.QtWidgets import QDesktopWidget
    # geometry of the main window
    qr = wid.frameGeometry()

    # center point of screen
    cp = QDesktopWidget().availableGeometry().center()

    # move rectangle's center point to screen's center point
    qr.moveCenter(cp)

    # top left of rectangle becomes top left of window centering it
    wid.move(qr.topLeft())


def plot_map(auth=("admin", "admin"), port_name="Alicante"):
    import os.path
    filename = "images/ports/" + port_name + ".png"

    if os.path.exists(filename):
        return filename

    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    _lat, _lon = db.ports.find_one({"name": port_name})["location"].split(", ")
    # _lat, _lon = "36°46'50\"N., 3°04'11\"E.".split(", ")
    # print(parse_dms(_lat), parse_dms(_lon))

    lat = parse_dms(_lat)
    lon = parse_dms(_lon)

    fig = plt.figure(figsize=(3, 3))
    m = Basemap(
        projection='lcc', resolution=None,
        width=8E6, height=8E6,
        lat_0=(180 + lat + 10 * lat / abs(lat)) % 360 - 180,
        lon_0=(180 + lon + 20 * lat / abs(lat)) % 360 - 180,
    )
    # m.etopo(scale=0.5, alpha=0.5)
    # m.drawlsmask(land_color='#80CBC4', ocean_color='#546E7A', lakes=True)
    m.drawlsmask(land_color='#80CBC4', ocean_color='#263238', lakes=True)

    # Map (long, lat) to (x, y) for plotting
    x, y = m(lon, lat)
    plt.plot(x, y, 'ok', markersize=3, color="#FFFFFF")
    plt.text(x + 5, y + 5, port_name, fontsize=12, color="#FFFFFF")

    # plt.show()
    plt.savefig(
        filename,
        transparent=True,
        frameon=False,
    )
    plt.close()
    return filename


# Used to convert GPS from degrees to decimal
def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd


def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]


def parse_dms(dms):
    parts = re.split('[°\'\"\.]', dms)
    # print(parts)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    return lat
# End of GPS convert


def gen_load_schedule(auth, ship_name, path, started):
    import datetime as dt
    import random

    def load_unload(pier_id, load, start_time):
        rate = db.piers.find({'_id': pier_id}).limit(1)[0]['rate']
        end_time = start_time + dt.timedelta(hours=load / rate)

        return end_time

    def voyage_time(ship_speed, distance, start_time):
        end_time = start_time + dt.timedelta(hours=distance / ship_speed)
        return end_time

    def rest_time(start_time):
        end_time = start_time + dt.timedelta(days=round(random.triangular(0, 10, mode=2)))
        return end_time

    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    ship = db.ships.find({"name": ship_name}).limit(1)[0]
    ship_id    = ship["_id"]
    size_type  = ship["size_type_id"]
    ship_type  = ship["ship_type_id"]
    ship_speed = ship["avg_speed"]

    print(size_type)

    load = random.triangular(
        0,
        db.sizes.find_one({"_id": size_type})["max_amount"],
        db.sizes.find_one({"_id": size_type})["max_amount"] - 100000.0
    )
    schedule = []

    schd_sample = {
        "destination_id" : None,
        "pier_id"        : None,
        "anchorage_id"   : None,
        "started"        : dt.date.today(),
        "estimated_end"  : dt.date.today(),
        "ship_id"        : None,
        "status"         : None
    }

    jobs = {
        "rest"  : db.jobs.find({"job": "RESTING"}).limit(1)[0]["_id"],
        "load"  : db.jobs.find({"job": "LOADING"}).limit(1)[0]["_id"],
        "unload": db.jobs.find({"job": "UNLOADING"}).limit(1)[0]["_id"],
        "voyage": db.jobs.find({"job": "VOYAGE"}).limit(1)[0]["_id"],
    }

    statuses = {
        "pen" : db.statuses.find({"status": "PENDING"}).limit(1)[0]["_id"],
        "fin" : db.statuses.find({"status": "FINISHED"}).limit(1)[0]["_id"],
        "prg" : db.statuses.find({"status": "IN_PROGRESS"}).limit(1)[0]["_id"]
    }

    ports = [db.ports.find_one({"name": p}) for p in path]

    schd = schd_sample

    starts = dt.datetime.combine(started, dt.datetime.min.time())
    ends   = rest_time(starts)

    schd["destination_id"] = None
    schd["pier_id"]        = None
    schd["anchorage_id"]   = db.anchorages.find_one({"port_id": ports[0]["_id"]})["_id"]
    schd["started"]        = starts
    schd["ship_id"]        = ship_id
    schd["estimated_end"]  = ends
    schd["job"]            = jobs["rest"]
    if starts > dt.datetime.now():
        schd["status"]     = statuses["pen"]
    elif ends < dt.datetime.now():
        schd["status"]     = statuses["fin"]
    else:
        schd["status"]     = statuses["prg"]

    schedule.append(schd.copy())

    starts = ends

    for i in range(1, len(ports) - 2):
        schd = schd_sample

        dest = db.destinations.find_one({"departure": ports[i - 1]["_id"], "destination": ports[i]["_id"]})
        ends = voyage_time(ship_speed, dest["distance"], starts)

        schd["destination_id"] = dest["_id"]
        schd["pier_id"]        = None
        schd["anchorage_id"]   = None
        schd["started"]        = starts
        schd["ship_id"]        = ship_id
        schd["estimated_end"]  = ends
        schd["job"]            = jobs["voyage"]
        if starts > dt.datetime.now():
            schd["status"]     = statuses["pen"]
        elif ends < dt.datetime.now():
            schd["status"]     = statuses["fin"]
        else:
            schd["status"]     = statuses["prg"]

        schedule.append(schd.copy())

        starts = ends

        schd = schd_sample

        ends = rest_time(starts)

        schd["destination_id"] = None
        schd["pier_id"]        = None
        schd["anchorage_id"]   = db.anchorages.find_one({"port_id": ports[i + 1]["_id"]})["_id"]
        schd["started"]        = starts
        schd["ship_id"]        = ship_id
        schd["estimated_end"]  = ends
        schd["job"]            = jobs["rest"]
        if starts > dt.datetime.now():
            schd["status"]     = statuses["pen"]
        elif ends < dt.datetime.now():
            schd["status"]     = statuses["fin"]
        else:
            schd["status"]     = statuses["prg"]

        schedule.append(schd.copy())

        starts = ends

    schd = schd_sample

    pier_id = db.piers.find_one({"port_id": ports[len(ports) - 1]["_id"], "pier_type": ship_type})["_id"]
    ends = load_unload(pier_id, load, starts)

    schd["destination_id"] = None
    schd["pier_id"]        = pier_id
    schd["anchorage_id"]   = None
    schd["started"]        = starts
    schd["ship_id"]        = ship_id
    schd["estimated_end"]  = ends
    schd["job"]            = jobs["load"]
    if starts > dt.datetime.now():
        schd["status"]     = statuses["pen"]
    elif ends < dt.datetime.now():
        schd["status"]     = statuses["fin"]
    else:
        schd["status"]     = statuses["prg"]

    schedule.append(schd.copy())

    return schedule