from utils import *

port_journal_sample = {
    "date"     : None,
    "port_id"  : None,
    "pier_id"  : None,
    "ship_id"  : None,
    "operation": None
}


def gen_port_journals(db, amount=5):
    import datetime as dt
    from tqdm import tqdm

    db.port_journals.drop()

    ptjn_list = []

    start_date = db.schedules.find_one(sort=[("started", 1)])["started"]
    end_date   = db.schedules.find_one(sort=[("estimated_end", -1)])["estimated_end"]

    delta = end_date - start_date

    pbar = tqdm(total=delta.days + 1, desc=" Generating port journals")

    date = start_date
    while date <= end_date + dt.timedelta(days=1):
        date_list = []
        get_events = list(db.schedules.find(
            {
                "$and": [
                    {"destination_id" : None},
                    {"started"        : {"$lte": date}},
                    {"estimated_end"  : {"$gte": date}},
                ]
            }
        ))
        if len(get_events) == 0:
            date += dt.timedelta(days=1)
            pbar.update()
            continue

        for event in get_events:
            pj = port_journal_sample

            if event["pier_id"]:
                port_id = db.piers.find_one({"_id": event["pier_id"]})["port_id"]
            else:
                port_id = db.anchorages.find_one({"_id": event["anchorage_id"]})["port_id"]

            pj = {
                "date"          : date,
                "port_id"       : port_id,
                "pier_id"       : event["pier_id"],
                "anchorage_id"  : event["anchorage_id"],
                "ship_id"       : event["ship_id"],
                "operation"     : event["job"]
            }

            date_list.append(pj.copy())
        coll_from_list(db.port_journals, date_list)

        ptjn_list.extend(date_list.copy())
        date += dt.timedelta(days=1)
        pbar.update()

    pbar.close()

    return ptjn_list
