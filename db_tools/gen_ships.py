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


def gen_crgos():
    crgos = ["Container", "Liquid", "Bulk"]

    crgo_id   = 0
    crgo_list = []

    for crgo in crgos:
        s = crgo_sample

        s["_id"]  = crgo_id
        s["type"] = crgo

        crgo_id += 1

        crgo_list.append(s.copy())

    return crgo_list


def gen_sizes():
    size_list = [
        {"_id": 0, "name": "LR1"    , "max_amount": 500000.0 },
        {"_id": 1, "name": "Aframax", "max_amount": 750000.0 },
        {"_id": 2, "name": "Suezmax", "max_amount": 1000000.0},
        {"_id": 3, "name": "VLCC"   , "max_amount": 2000000.0},
        {"_id": 4, "name": "ULCC"   , "max_amount": 4000000.0}
    ]
    return size_list


def gen_rand_ship(port_list, crgo_list, cntr_list, size_list):
    import random
    import names

    ship = ship_sample

    size_type = round(random.triangular(0, len(size_list) - 1, 1))

    ship["name"]         = names.get_full_name()
    ship["avg_speed"]    = random.uniform(10 - size_type, 24 - size_type)
    ship["home_port_id"] = port_list[random.randint(0, len(port_list) - 1)]["_id"]
    ship["ship_type_id"] = crgo_list[random.randint(0, len(crgo_list) - 1)]["_id"]
    ship["flag_id"]      = cntr_list[random.randint(0, len(cntr_list) - 1)]["_id"]
    ship["cargo_amount"] = random.triangular(
        0,
        size_list[size_type]["max_amount"],
        size_list[size_type]["max_amount"] - 100000.0
    )
    ship["size_type_id"] = str(size_list[size_type]["_id"])

    return ship


def gen_ships(port_list, crgo_list, cntr_list, size_list, amount=50):
    from tqdm import tqdm

    ship_list = []

    pbar = tqdm(total=amount, desc="Generating ships")

    for _id in range(amount):
        ship = gen_rand_ship(port_list, crgo_list, cntr_list, size_list)

        pbar.update()
        ship_list.append(ship.copy())

    pbar.close()

    return ship_list
