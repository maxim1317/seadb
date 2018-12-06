from utils import *


def gen_stats(db):
    db.statuses.drop()

    stat_list = [
        {"status": "FINISHED"   },
        {"status": "PENDING"    },
        {"status": "IN_PROGRESS"},
        {"status": "CANCELED"   },
        {"status": "ЕГГОГ"      },
    ]
    stat_coll = db.statuses

    coll_from_list(stat_coll, stat_list)
    return stat_list


def gen_jobs(db):
    db.jobs.drop()

    job_list = [
        {"job": "VOYAGE"   },
        {"job": "RESTING"  },
        {"job": "LOADING"  },
        {"job": "UNLOADING"},
    ]
    job_coll = db.jobs

    coll_from_list(job_coll, job_list)
    return job_list


crgo_sample = {
    "type"         : "some_type"
}

size_sample = {
    "type"         : "some_type"
}


def gen_crgos(db):
    crgos = ["Container", "Liquid", "Bulk"]

    db.cargo_types.drop()

    crgo_list = []
    crgo_coll = db.cargo_types

    for crgo in crgos:
        s = crgo_sample

        s["type"] = crgo

        crgo_list.append(s.copy())

    coll_from_list(crgo_coll, crgo_list)

    return crgo_list


def gen_sizes(db):
    db.sizes.drop()

    size_coll = db.sizes
    size_list = [
        {"no": 0, "name": "LR1"    , "max_amount": 500000.0 },
        {"no": 1, "name": "Aframax", "max_amount": 750000.0 },
        {"no": 2, "name": "Suezmax", "max_amount": 1000000.0},
        {"no": 3, "name": "VLCC"   , "max_amount": 2000000.0},
        {"no": 4, "name": "ULCC"   , "max_amount": 4000000.0}
    ]

    coll_from_list(size_coll, size_list)
    return size_list
