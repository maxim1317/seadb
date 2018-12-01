from utils import *


nav_db = '../resources/PUB151_distances.json'

ships = "../db/ships.json"
dests = "../db/dests.json"


def gen_ports_and_dests():

    port_sample = {
        "name"       : "some_name",
        "country_id" : 0,
        "location"   : "27°05'37\"N., 13°26'55\"W."
    }

    dest_sample = {
        "departure"  : 0,
        "destination": 0,
        "distance"   : 0.0
    }

    off_data = json_to_dict(nav_db)

    for port_name, data in off_data.iteritems():
        port = port_sample

        port["name"]     = port_name
        port["location"] = data["location"]

        for dest in data["destinations"]
