from pymongo import MongoClient

DB_NAME = 'seadb'


def get_ship_list():
    client = MongoClient()
    db = client[DB_NAME]

    ship_list = []
    all_ships = list(db.ships.find({}))

    for ship in all_ships:
        ship_list.append(ship["name"])

    client.close()
    return ship_list


def get_port_list():
    client = MongoClient()
    db = client[DB_NAME]

    port_list = []
    all_ports = list(db.ports.find({}))

    for port in all_ports:
        port_list.append(port["name"])

    client.close()
    return port_list


def get_top_10_dict():
    client = MongoClient()
    db = client[DB_NAME]



    return top_10


def get_top_10_items():
    top_10_items = []

    return top_10_items

