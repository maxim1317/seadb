ship_sample = {
    "_id"          : 0,
    "name"         : "some_name",
    "avg_speed"    : 0,
    "home_port_id" : 0,
    "ship_type_id" : 0,
    "flag_id"      : 0
}

shtp_sample = {
    "_id"          : 0,
    "type"         : "some_type"
}


def gen_shtps():
    shtps = ["Container", "Liquid", "Bulk"]

    shtp_id   = 0
    shtp_list = []

    for shtp in shtps:
        s = shtp_sample

        s["_id"]  = shtp_id
        s["type"] = shtp

        shtp_id += 1

        shtp_list.append(s.copy())

    return shtp_list


def gen_ships(port_list, shtp_list, cntr_list, amount=50):
    import random
    import names

    ship_list = []

    for _id in range(amount):
        ship = ship_sample

        ship["_id"]          = _id
        ship["name"]         = names.get_full_name()
        ship["avg_speed"]    = random.uniform(10, 25)
        ship["home_port_id"] = port_list[random.randint(0, len(port_list) - 1)]["_id"]
        ship["ship_type_id"] = shtp_list[random.randint(0, len(shtp_list) - 1)]["_id"]
        ship["flag_id"]      = cntr_list[random.randint(0, len(cntr_list) - 1)]["_id"]

        ship_list.append(ship.copy())

    return ship_list
