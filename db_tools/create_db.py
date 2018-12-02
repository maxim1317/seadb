from pymongo import MongoClient

from utils import *

ports_file = "../resources/json/ports.json"
dests_file = "../resources/json/dests.json"
cntrs_file = "../resources/json/cntrs.json"
shtps_file = "../resources/json/shtps.json"
ships_file = "../resources/json/ships.json"


DB_NAME = 'seadb'


def coll_from_list(coll, import_list):
    coll.insert_many(import_list)
    return


def create_db():
    client = MongoClient()
    db = client.drop_database(DB_NAME)
    db = client[DB_NAME]

    ports = db["ports"]
    dests = db["destinations"]
    cntrs = db["countries"]
    shtps = db["cargo_types"]
    ships = db["ships"]

    port_list = json_to_list(ports_file)
    dest_list = json_to_list(dests_file)
    cntr_list = json_to_list(cntrs_file)
    shtp_list = json_to_list(shtps_file)
    ship_list = json_to_list(ships_file)

    coll_from_list(ports, port_list)
    coll_from_list(dests, dest_list)
    coll_from_list(cntrs, cntr_list)
    coll_from_list(shtps, shtp_list)
    coll_from_list(ships, ship_list)

    return


create_db()
