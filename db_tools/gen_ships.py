from utils import *
ship_sample = {
    "name"         : "some_name",
    "avg_speed"    : 0,
    "home_port_id" : 0,
    "ship_type_id" : 0,
    "flag_id"      : 0,
    "size_type_id" : 0,
    "cargo_amount" : 0.0
}

crgo_sample = {
    "type"         : "some_type"
}

size_sample = {
    "type"         : "some_type"
}


def gen_crgos(db):
    crgos = ["Container", "Liquid", "Bulk"]

    crgo_coll = db.cargo_types

    crgo_id   = 0
    crgo_list = []

    for crgo in crgos:
        s = crgo_sample

        s["type"] = crgo

        crgo_id += 1

        crgo_list.append(s.copy())

    coll_from_list(crgo_coll, crgo_list)

    return crgo_list


def gen_sizes(db):
    size_coll = db.sizes
    size_list = [
        {"no": 0, "name": "LR1"    , "max_amount": 500000.0 },
        {"no": 1, "name": "Aframax", "max_amount": 750000.0 },
        {"no": 2, "name": "Suezmax", "max_amount": 1000000.0},
        {"no": 3, "name": "VLCC"   , "max_amount": 2000000.0},
        {"no": 4, "name": "ULCC"   , "max_amount": 4000000.0}
    ]

    coll_from_list(size_coll, size_list)
    return size_list


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
    ship["cargo_amount"] = random.triangular(
        0,
        db.sizes.find_one({"no": size_type})["max_amount"],
        db.sizes.find_one({"no": size_type})["max_amount"] - 100000.0
    )
    ship["size_type_id"] = db.sizes.find_one({"no": size_type})["_id"]

    return ship


def gen_ships(db, amount=50):
    from tqdm import tqdm

    ship_coll = db.ships
    ship_list = []

    pbar = tqdm(total=amount, desc="Generating ships")

    for _id in range(amount):
        ship = gen_rand_ship(db)

        pbar.update()
        ship_list.append(ship.copy())

    coll_from_list(ship_coll, ship_list)
    pbar.close()

    return ship_list
