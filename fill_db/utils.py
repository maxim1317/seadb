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
