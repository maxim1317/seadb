from pymongo import MongoClient

from utils import *

ports_file = "../resources/json/ports.json"
dests_file = "../resources/json/dests.json"
cntrs_file = "../resources/json/cntrs.json"
crgos_file = "../resources/json/crgos.json"
ships_file = "../resources/json/ships.json"
sizes_file = "../resources/json/sizes.json"


DB_NAME = 'seadb'


def coll_from_list(coll, import_list):
    coll.insert_many(import_list)
    return


def create_coll_ship(db):
    ports = db["ports"]
    ports.create_index(["name"], unique=True)
    return db


def create_db():
    client = MongoClient()
    db = client.drop_database(DB_NAME)
    db = client[DB_NAME]

    ports = db["ports"]
    dests = db["destinations"]
    cntrs = db["countries"]
    crgos = db["cargo_types"]
    ships = db["ships"]
    sizes = db["sizes"]

    port_list = json_to_list(ports_file)
    dest_list = json_to_list(dests_file)
    cntr_list = json_to_list(cntrs_file)
    crgo_list = json_to_list(crgos_file)
    ship_list = json_to_list(ships_file)
    size_list = json_to_list(sizes_file)

    coll_from_list(ports, port_list)
    coll_from_list(dests, dest_list)
    coll_from_list(cntrs, cntr_list)
    coll_from_list(crgos, crgo_list)
    coll_from_list(ships, ship_list)
    coll_from_list(sizes, size_list)

    return


create_db()
