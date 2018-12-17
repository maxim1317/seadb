from pymongo import MongoClient, errors

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


def collect_ship_info(name, auth):
    login, password = auth
    client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
    db = client[DB_NAME]

    ship = db.ships.find_one({"name": name})

    info = {
        "name"         : name,
        "avg_speed"    : ship["avg_speed"],
        "home_port"    : db.ports.find_one({"_id": ship["home_port_id"]})["name"],
        "ship_type_id" : db.ports.find_one({"_id": ship["home_port_id"]})["name"],
        "flag_id"      : db.ports.find_one({"_id": ship["home_port_id"]})["name"],
        "size_type_id" : db.ports.find_one({"_id": ship["home_port_id"]})["name"],
        "cargo_amount" : db.ports.find_one({"_id": ship["home_port_id"]})["name"]
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
