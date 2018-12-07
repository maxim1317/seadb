from pymongo import MongoClient

from gen_open_data import *
from gen_consts import *
from gen_first import *
from gen_second import *
from gen_third import *
from gen_utilities import *

from utils import *


DB_NAME = 'seadb'


def gen_one(db, gen, amount=None):
    from termcolor import colored

    gens = {
        "ships": {
            "fn"  : gen_ships,
            "json": "../resources/json/ships.json",
            "name": "ships"
        },
        "countries": {
            "fn"  : gen_cntrs,
            "json": "../resources/json/countries.json",
            "name": "countries"
        },
        "ports": {
            "fn"  : gen_ports,
            "json": "../resources/json/ports.json",
            "name": "ports"
        },
        "piers": {
            "fn"  : gen_piers,
            "json": "../resources/json/piers.json",
            "name": "piers"
        },
        "cargo_types": {
            "fn"  : gen_crgos,
            "json": "../resources/json/cargo_types.json",
            "name": "cargo_types"
        },
        "sizes": {
            "fn"  : gen_sizes,
            "json": "../resources/json/sizes.json",
            "name": "sizes"
        },
        "destinations": {
            "fn"  : gen_dests,
            "json": "../resources/json/destinations.json",
            "name": "destinations"
        },
        "jobs": {
            "fn"  : gen_jobs,
            "json": "../resources/json/jobs.json",
            "name": "jobs"
        },
        "statuses": {
            "fn"  : gen_stats,
            "json": "../resources/json/statuses.json",
            "name": "statuses"
        },
        "schedules": {
            "fn"  : gen_schedules,
            "json": "../resources/json/schedules.json",
            "name": "schedules"
        },
        "anchorages": {
            "fn"  : gen_anchorages,
            "json": "../resources/json/anchorages.json",
            "name": "anchorages"
        },
        "ch_dests": {
            "fn"  : check_dests,
            "json": "../resources/json/ch_dests.json",
            "name": "ch_dests"
        },
        "ch_ports": {
            "fn"  : check_ports,
            "json": "../resources/json/ch_ports.json",
            "name": "ch_ports"
        },
        "utils"   : {
            "fn"  : gen_utils,
            "json": "../resources/json/utils.json",
            "name": "utilities"
        }
    }
    gen_list = []

    out = "Generating " + colored(gens[gen]["name"], 'yellow') + "..."
    print("\n", out, end=((50 - len(out)) * " " + "[" + colored("  WAIT  ", 'yellow') + "]\n"))

    if amount:
        gen_list = gens[gen]["fn"](db, amount)
    else:
        gen_list = gens[gen]["fn"](db)

    out = "Generating " + colored(gens[gen]["name"], 'yellow') + "..."
    if len(gen_list):
        print("", out, end=((50 - len(out)) * " " + "[" + colored("   OK   ", 'green') + "]\n"))
    else:
        print("", out, end=((50 - len(out)) * " " + "[" + colored(" FAILED ", 'red') + "]\n"))

    return gen_list


def db_generator(groups_to_gen):
    client = MongoClient()
    db = client[DB_NAME]

    colls = {
        "open_data": {
            "threaded" : False,
            "data"     : [
                {
                    "name"   : "countries",
                    "amount" : None
                },
                {
                    "name"   : "ports",
                    "amount" : None
                },
                {
                    "name"   : "destinations",
                    "amount" : None
                },
                {
                    "name"   : "ch_dests",
                    "amount" : None
                },
                {
                    "name"   : "ch_ports",
                    "amount" : None
                }
            ],
        },
        "consts"    : {
            "threaded" : True,
            "data"     : [
                {
                    "name"   : "sizes",
                    "amount" : None
                },
                {
                    "name"   : "cargo_types",
                    "amount" : None
                },
                {
                    "name"   : "jobs",
                    "amount" : None
                },
                {
                    "name"   : "statuses",
                    "amount" : None
                },
            ]
        },
        "first"     : {
            "threaded" : True,
            "data"     : [
                {
                    "name"   : "piers",
                    "amount" : 5
                },
                {
                    "name"   : "anchorages",
                    "amount" : None
                },
            ]
        },
        "second"    : {
            "threaded" : True,
            "data"     : [
                {
                    "name"   : "ships",
                    "amount" : 10000
                },
            ]
        },
        "third"     : {
            "threaded" : True,
            "data"     : [
                {
                    "name"   : "schedules",
                    "amount" : 5
                },
            ]
        },
        "utils"     : {
            "threaded" : True,
            "data"     : [
                {
                    "name"   : "utils",
                    "amount" : None
                },
            ]
        }
    }
    for group in groups_to_gen:
        for coll in colls[group]["data"]:
            if coll["amount"]:
                gen_one(db=db, gen=coll["name"], amount=coll["amount"])
            else:
                gen_one(db=db, gen=coll["name"])

    return 0


if __name__ == '__main__':
    to_gen = ["third"]
    db_generator(groups_to_gen=to_gen)
