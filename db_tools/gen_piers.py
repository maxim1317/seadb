pier_sample = {
    "port_id"   : 0,
    "pier_type" : 0,
    "rate"      : 0.0
}


def gen_piers(port_coll, crgo_coll, per_port_max=5):
    import random

    pier_list = []

    for port in port_coll.find():
        for pier in range(random.randint(1, per_port_max)):
            pier = pier_sample

            pier["port_id"]   = port["_id"]
            pier["pier_type"] = crgo_coll.find()[random.randint(crgo_coll.count_documents({}))]

    return pier_list
