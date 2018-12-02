def json_to_dict(json_path):
    '''
        Reads JSON file and returns a dict
    '''
    from json import loads

    with open(json_path) as raw:
        jdict = loads(raw.read())
    return jdict


def dict_to_json(jdict, json_path):
    '''
        Writes dict as JSON to file
    '''
    from json import dump

    with open(json_path, 'w') as raw:
        dump(jdict, raw, indent=4, sort_keys=False, ensure_ascii=False)
    return


def list_to_json(jlist, json_path):
    return dict_to_json(jlist, json_path)


def json_to_list(json_path):
    return json_to_dict(json_path)


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
