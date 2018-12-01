def json_to_dict(jsonPath):
    '''
        Reads JSON file and returns a dict
    '''
    from json import loads

    with open(jsonPath) as raw:
        jdict = loads(raw.read())
    return jdict


def dict_to_json(jdict, jsonPath):
    '''
        Writes dict as JSON to file
    '''
    from json import dump

    with open(jsonPath, 'w') as raw:
        dump(jdict, raw, indent=4, sort_keys=False)
    return
