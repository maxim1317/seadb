from tqdm import tqdm

from gen_ports_cntrs_dests import gen_ports
from gen_ships import gen_ships, gen_crgos, gen_sizes
from utils import *

ports_file = "../resources/json/ports.json"
dests_file = "../resources/json/dests.json"
cntrs_file = "../resources/json/cntrs.json"
crgos_file = "../resources/json/crgos.json"
ships_file = "../resources/json/ships.json"
sizes_file = "../resources/json/sizes.json"


def gen_all():
    pbar = tqdm(total=6, desc="Generating data ")

    port_list, cntr_list, dest_list = gen_ports()
    pbar.update(3)
    crgo_list = gen_crgos()
    pbar.update()
    size_list = gen_sizes()
    pbar.update()
    ship_list = gen_ships(port_list, crgo_list, cntr_list, size_list, amount=10000)
    pbar.update()
    pbar.close()

    # port_list = json_to_list(ports_file)
    # dest_list = json_to_list(dests_file)
    # cntr_list = json_to_list(cntrs_file)
    # crgo_list = json_to_list(crgos_file)
    # ship_list = json_to_list(ships_file)

    # pier_list = gen_piers(port_list)

    print('\n\n\n')

    list_to_json(port_list, ports_file)
    print("Ports added:        ", len(port_list))
    list_to_json(cntr_list, cntrs_file)
    print("Countries added:    ", len(cntr_list))
    list_to_json(dest_list, dests_file)
    print("Destinations added: ", len(dest_list))
    list_to_json(crgo_list, crgos_file)
    print("Cargo types added:  ", len(crgo_list))
    list_to_json(ship_list, ships_file)
    print("Ships added:        ", len(ship_list))
    list_to_json(size_list, sizes_file)
    print("Size types added:   ", len(size_list))


gen_all()
