from pymongo import MongoClient

DB_NAME = 'seadb'


def get_ship_list():
    client = MongoClient()
    db = client[DB_NAME]

    ship_list = []
    all_ships = list(db.ships.find({}))

    for ship in all_ships:
        ship_list.append(ship["name"])

    client.close()
    return ship_list
