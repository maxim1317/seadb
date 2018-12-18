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


def plot_map(auth, port_name):
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
    m.etopo(scale=0.5, alpha=0.5)

    # Map (long, lat) to (x, y) for plotting
    x, y = m(lon, lat)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, port_name, fontsize=12)

    # plt.show()
    plt.savefig(filename)
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
    print(parts)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    return lat
# End of GPS convert
