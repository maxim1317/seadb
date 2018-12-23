from pymongo import MongoClient

from utils import *
import random
import datetime as dt
import pprint


DB_NAME = 'seadb'
client = MongoClient()
# db = client.drop_database(DB_NAME)
db = client[DB_NAME]


# def port_graph(db):
#     import networkx as nx

#     G = nx.Graph()
#     dests = []

#     dests_raw = list(db.destinations.find({}))

#     for d in dests_raw:
#         dest = {
#             "from": db.ports.find_one({"_id": d["departure"]})["name"],
#             "to"  : db.ports.find_one({"_id": d["destination"]})["name"],
#             "dist": d["distance"]
#         }
#         dests.append(dest)

#     for d in dests:
#         G.add_edge(d["from"], d["to"], weight=d["dist"])

#     nx.write_yaml(G, "../app/images/graph.yaml")

def draw_graph(db):
    import networkx as nx

    G = nx.read_yaml("../app/images/graph.yaml")


pp = pprint.PrettyPrinter(indent=4)
draw_graph(db)
# pp.pprint(db.ships.find({"load": 0}))
# pp.pprint(db.anchorages.find({"port_id": dest["_id"]}).limit(1)[0]["_id"])
