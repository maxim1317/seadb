from utils import *

def gen_journals(db, amount=5):
    from tqdm import tqdm
    from threading import Thread

    db.journals.drop()
    for i in range(8):
        db["fock" + str(i)].drop()
        db["good_ports" + str(i)].drop()

    schd_list = []

    stops_list = list(db.schedules.find({}))
    pbar = tqdm(total=len(ship_list) * amount, desc=" Generating journals")

    threads = []
    for i in range(8):
        # schd = gen_rand_schd(db, amount=amount, ship_id=ship_list[i]["_id"], pbar=pbar)
        t = Thread(
            target=run_batch, args=(db, amount, ship_list, i, pbar)
        )
        threads.append(t)
        t.start()

        # pbar.update(amount)
        # schd_list.extend(schd.copy())

    for thread in threads:
        thread.join()

    pbar.close()

    return schd_list