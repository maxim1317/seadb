from utils import *
pier_sample = {
    "port_id"   : 0,
    "pier_type" : 0,
    "rate"      : 0.0
}
anch_sample = {
    "port_id": None
}


def gen_piers(db, amount=5):
    import random
    from tqdm import tqdm

    db.piers.drop()

    pier_list = []
    pier_coll = db.piers
    port_coll = db.ports
    crgo_coll = db.cargo_types

    pbar = tqdm(total=port_coll.count(), desc=" Generating piers")

    for port in port_coll.find():
        for pier in range(random.randint(1, amount)):
            pier = pier_sample

            k = 750000.0 / 24
            k_left  = k / 3
            k_right = k / 10

            pier["port_id"]   = port["_id"]
            pier["pier_type"] = list(crgo_coll.find())[random.randint(0, crgo_coll.count() - 1)]["_id"]
            pier["rate"]      = random.triangular(k_left, k_right, k / 5)

            pier_list.append(pier.copy())
        pbar.update()

    pbar.close()

    coll_from_list(pier_coll, pier_list)
    return pier_list


def gen_anchorages(db):
    db.anchorages.drop()

    anch_list = []
    anch_coll = db.anchorages

    ports = list(db.ports.find({}))
    for port in ports:
        anch = anch_sample
        anch["port_id"] = port["_id"]
        anch_list.append(anch.copy())

    coll_from_list(anch_coll, anch_list)
    return anch_list
