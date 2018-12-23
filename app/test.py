from pymongo import MongoClient
from tqdm import tqdm
from ut import *


client = MongoClient()
db = client[DB_NAME]

ports = list(db.ports.find({}))

pbar = tqdm(total=len(ports))
for port in ports:
    plot_map(port_name=port["name"])
    pbar.update()
pbar.close()
