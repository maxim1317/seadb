from utils import *
from tqdm import tqdm


nav_db = '../resources/PUB151_distances.json'


def gen_country(country, cntr_list):

    cntr_sample = {
        "name"       : "some_name"
    }

    in_cntr_list = False
    for cntr in cntr_list:
        if country == cntr["name"]:
            in_cntr_list = True
            break
    if not in_cntr_list:
        cntr = cntr_sample
        cntr["name"] = country

        cntr_list.append(cntr)

    return cntr_list


def gen_cntrs(db):

    db.countries.drop()

    cntr_list = []
    cntr_coll = db.countries

    off_data = json_to_dict(nav_db)
    for port_name, data in off_data.items():

        port_name_split = port_name.split(',')
        country = port_name_split[-1].lstrip().rstrip()

        cntr_list = gen_country(country, cntr_list)

    coll_from_list(cntr_coll, cntr_list)

    return cntr_list


def gen_ports(db):
    db.ports.drop()

    port_list = []
    port_coll = db.ports

    port_sample = {
        "name"       : "some_name",
        "country_id" : 0,
        "location"   : "27°05'37\"N., 13°26'55\"W."
    }

    off_data = json_to_dict(nav_db)
    for port_name, data in off_data.items():
        port = port_sample

        port_name_split = port_name.split(',')
        name    = port_name_split[0].lstrip().rstrip()
        country = port_name_split[-1].lstrip().rstrip()

        port["name"]       = name
        port["country_id"] = db.countries.find_one({'name' : country})["_id"]
        port["location"]   = data["location"]

        port_list.append(port.copy())

    coll_from_list(port_coll, port_list)

    return port_list


def gen_dests(db):

    db.destinations.drop()

    dest_list = []
    dest_coll = db.destinations

    dest_sample = {
        "departure"  : 0,
        "destination": 0,
        "distance"   : 0.0
    }

    off_data = json_to_dict(nav_db)

    pbar = tqdm(total=len(off_data.keys()), desc=" Generating destinations")

    for port_name, data in off_data.items():

        port_name_split = port_name.split(',')
        name = port_name_split[0].lstrip().rstrip()

        # print(data["destinations"])

        if not isinstance(data["destinations"], str):

            for destination, distance in data["destinations"].items():
                d = dest_sample
                dest_name = destination.lstrip().rstrip().rsplit(' ', 1)[0]
                d["departure"]   = find_doc(name, db.ports)
                destination = find_doc(dest_name, db.ports)
                if destination == -1:
                    continue
                d["destination"] = destination
                d["distance"]    = distance

                dest_list.append(d.copy())

        if not isinstance(data["junctions"], str):

            for destination, distance in data["junctions"].items():
                d = dest_sample
                dest_name = destination.lstrip().rstrip().rsplit(' ', 1)[0]
                d["departure"]   = find_doc(name, db.ports)
                destination = find_doc(dest_name, db.ports)
                if destination == -1:
                    continue
                d["destination"] = destination
                d["distance"]    = distance

                dest_list.append(d.copy())

        pbar.update()
    pbar.close()

    coll_from_list(dest_coll, dest_list)

    return dest_list


def check_dests(db):
    dests = list(db.destinations.find({}))
    new = []

    pbar = tqdm(total=len(dests), desc=" Checking destinations")
    for dest in dests:
        dep = dest["departure"]
        des = dest["destination"]
        dist = dest["distance"]
        if db.destinations.count_documents({'$and': [
            {'destination': dep}, {'departure': des}
        ]}) == 0:
            doc = {
                "departure"  : des,
                "destination": dep,
                "distance"   : dist
            }
            db.destinations.insert_one(doc)
            new.append(doc.copy())
        pbar.update()
    pbar.close()
    return new


def check_ports(db):
    ports = list(db.ports.find({}))
    count = 0

    pbar = tqdm(total=len(ports), desc=" Checking ports")
    for port in ports:
        _id = port["_id"]
        if db.destinations.count_documents({'departure': _id}) == 0:
            db.ports.delete_one({'_id': _id})
            count += 1

        pbar.update()
    pbar.close()
    return [count]
