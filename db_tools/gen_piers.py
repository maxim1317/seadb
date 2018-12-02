pier_sample = {
    "port_id"   : 0,
    "pier_type" : 0,
    "rate"      : 0.0
}


def gen_piers(port_coll, crgo_coll, max_per_port=5):
    import random
    from tqdm import tqdm

    pier_list = []

    pbar = tqdm(total=port_coll.count(), desc="Generating piers")

    for port in port_coll.find():
        for pier in range(random.randint(1, max_per_port)):
            pier = pier_sample

            k = 750000.0 / 24
            k_left  = k / 3
            k_right = k / 10

            pier["port_id"]   = str(port["_id"])
            pier["pier_type"] = list(crgo_coll.find())[random.randint(0, crgo_coll.count() - 1)]["_id"]
            pier["rate"]      = random.triangular(k_left, k_right, k / 5)

            pier_list.append(pier.copy())
        pbar.update()

    pbar.close()

    return pier_list
