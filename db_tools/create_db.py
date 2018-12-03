from pymongo import MongoClient
from tqdm import tqdm

from gen_ports_cntrs_dests import *
from gen_ships import *
from gen_piers import *

from utils import *

ports_file = "../resources/json/ports.json"
dests_file = "../resources/json/dests.json"
cntrs_file = "../resources/json/cntrs.json"
crgos_file = "../resources/json/crgos.json"
ships_file = "../resources/json/ships.json"
sizes_file = "../resources/json/sizes.json"
piers_file = "../resources/json/piers.json"


DB_NAME = 'seadb'


def create_coll_ship(db):
    ports = db["ports"]
    ports.create_index(["name"], unique=True)
    return db


def create_db(gen=False):
    client = MongoClient()
    db = client.drop_database(DB_NAME)
    db = client[DB_NAME]

    ports = db["ports"]
    dests = db["destinations"]
    cntrs = db["countries"]
    crgos = db["cargo_types"]
    ships = db["ships"]
    sizes = db["sizes"]
    piers = db["piers"]

    if gen:
        pbar = tqdm(total=7, desc="Generating data ")

        cntr_list = gen_cntrs(db)
        pbar.update()
        port_list = gen_ports(db)
        pbar.update()
        dest_list = gen_dests(db)
        pbar.update()
        crgo_list = gen_crgos(db)
        pbar.update()
        size_list = gen_sizes(db)
        pbar.update()
        ship_list = gen_ships(db, amount=200)
        pbar.update()

    else:
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

    if gen:
        pier_list = gen_piers(ports, crgos, max_per_port=10)
        pbar.update()
        pbar.close()
    else:
        pier_list = json_to_list(piers_file)

    coll_from_list(piers, pier_list)

    print('\n\n\n')

    list_to_json(serealize(port_list), ports_file)
    print("Ports generated:        ", len(port_list))
    list_to_json(serealize(cntr_list), cntrs_file)
    print("Countries generated:    ", len(cntr_list))
    list_to_json(serealize(dest_list), dests_file)
    print("Destinations generated: ", len(dest_list))
    list_to_json(serealize(crgo_list), crgos_file)
    print("Cargo types generated:  ", len(crgo_list))
    list_to_json(serealize(ship_list), ships_file)
    print("Ships generated:        ", len(ship_list))
    list_to_json(serealize(size_list), sizes_file)
    print("Size types generated:   ", len(size_list))
    list_to_json(serealize(pier_list), piers_file)
    print("Piers generated:        ", len(pier_list))

    return


create_db(gen=True)
# create_db()
