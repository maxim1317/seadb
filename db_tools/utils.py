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


def find_doc(name, coll):
    # print(coll.find_one({'name': name}))
    if coll.count({'name': name}) != 0:
        return coll.find({'name': name}).limit(1)[0]["_id"]
    else:
        return -1


def serealize(some_list):
    import bson

    for item in some_list:
        for key, value in item.items():
            if bson.objectid.ObjectId.is_valid(value):
                item[key] = str(item[key])

    return some_list


def coll_from_list(coll, import_list):
    coll.insert_many(import_list)
    return
