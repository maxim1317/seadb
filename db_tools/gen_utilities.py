def gen_utils(db):
    import datetime
    db.utils.drop()

    db.utils.insert_one({'last_upd': datetime.datetime.now()})

    return []
