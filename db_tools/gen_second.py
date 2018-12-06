from utils import *
from tqdm import tqdm

ship_sample = {
    "name"         : "some_name",
    "avg_speed"    : 0,
    "home_port_id" : 0,
    "ship_type_id" : 0,
    "flag_id"      : 0,
    "size_type_id" : 0,
    "cargo_amount" : 0.0
}


def gen_rand_ship(db):
    import random
    import names

    ship = ship_sample

    size_type = round(random.triangular(0, db.sizes.count() - 1, 1))

    ship["name"]         = names.get_full_name()
    ship["avg_speed"]    = random.uniform(10 - size_type, 24 - size_type)
    ship["home_port_id"] = db.ports.find({})[random.randint(0, db.ports.count() - 1)]["_id"]
    ship["ship_type_id"] = db.cargo_types.find({})[random.randint(0, db.cargo_types.count() - 1)]["_id"]
    ship["flag_id"]      = db.countries.find({})[random.randint(0, db.countries.count() - 1)]["_id"]
    ship["cargo_amount"] = 0
    ship["size_type_id"] = db.sizes.find_one({"no": size_type})["_id"]

    return ship


def gen_ships(db, amount=50):

    db.ships.drop()
    ship_coll = db.ships
    ship_list = []

    pbar = tqdm(total=amount, desc=" Generating ships")

    for _id in range(amount):
        ship = gen_rand_ship(db)

        pbar.update()
        ship_list.append(ship.copy())

    coll_from_list(ship_coll, ship_list)
    pbar.close()

    return ship_list
