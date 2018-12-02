from gen_ports_cntrs_dests import gen_ports
from gen_ships import gen_ships, gen_shtps
from utils import *

ports = "../resources/json/ports.json"
dests = "../resources/json/dests.json"
cntrs = "../resources/json/cntrs.json"
shtps = "../resources/json/shtps.json"
ships = "../resources/json/ships.json"


def gen_all():
    port_list, cntr_list, dest_list = gen_ports()
    shtp_list = gen_shtps()
    ship_list = gen_ships(port_list, shtp_list, cntr_list, amount=20000)

    list_to_json(port_list, ports)
    print("Ports added:        ", len(port_list))
    list_to_json(cntr_list, cntrs)
    print("Countries added:    ", len(cntr_list))
    list_to_json(dest_list, dests)
    print("Destinations added: ", len(dest_list))
    list_to_json(shtp_list, shtps)
    print("Ship types added:   ", len(shtp_list))
    list_to_json(ship_list, ships)
    print("Ships added:        ", len(ship_list))


