from utils import *


nav_db = '../resources/PUB151_distances.json'

ports = "../resources/json/ports.json"
dests = "../resources/json/dests.json"
cntrs = "../resources/json/cntrs.json"


def add_country(country, cntr_id, cntr_list):

    cntr_sample = {
        "_id"        : 0,
        "name"       : "some_name"
    }

    in_cntr_list = False
    for cntr in cntr_list:
        if country == cntr["name"]:
            in_cntr_list = True
            break
    if not in_cntr_list:
        cntr = cntr_sample
        cntr["_id"]  = cntr_id
        cntr["name"] = country

        cntr_list.append(cntr)

        cntr_id += 1
    return cntr_id, cntr_list


def find_country(country, cntr_list):
    for cntr in cntr_list:
        if country == cntr["name"]:
            return cntr["_id"]

    return -1


def find_port(name, port_list):
    for port in port_list:
        if name == port["name"]:
            return port["_id"]

    return -1


def gen_ports():

    port_sample = {
        "_id"        : 0,
        "name"       : "some_name",
        "country_id" : 0,
        "location"   : "27°05'37\"N., 13°26'55\"W."
    }

    dest_sample = {
        "_id"        : 0,
        "departure"  : 0,
        "destination": 0,
        "distance"   : 0.0
    }

    port_id = 0
    dest_id = 0
    cntr_id = 0

    port_list = []
    dest_list = []
    cntr_list = []

    off_data = json_to_dict(nav_db)

    for port_name, data in off_data.items():
        port = port_sample

        port_name_split = port_name.split(',')
        name    = port_name_split[0].lstrip().rstrip()
        country = port_name_split[-1].lstrip().rstrip()

        cntr_id, cntr_list = add_country(country, cntr_id, cntr_list)

        port["_id"]        = port_id
        port["name"]       = name
        port["country_id"] = find_country(country, cntr_list)
        port["location"]   = data["location"]

        port_list.append(port.copy())

        port_id += 1

    for port_name, data in off_data.items():

        port_name_split = port_name.split(',')
        name = port_name_split[0].lstrip().rstrip()

        # print(data["destinations"])

        if isinstance(data["destinations"], str):
            continue

        for destination, distance in data["destinations"].items():
            d = dest_sample
            dest_name = destination.lstrip().rstrip().rsplit(' ', 1)[0]
            d["_id"]         = dest_id
            d["departure"]   = find_port(name, port_list)
            if find_port(dest_name, port_list) == -1:
                continue
            d["destination"] = find_port(dest_name, port_list)
            d["distance"]    = distance

            dest_list.append(d.copy())

            dest_id += 1

    list_to_json(port_list, ports)
    print("Ports added:        ", len(port_list))
    list_to_json(cntr_list, cntrs)
    print("Countries added:    ", len(cntr_list))
    list_to_json(dest_list, dests)
    print("Destinations added: ", len(dest_list))

    return 0


gen_ports()
