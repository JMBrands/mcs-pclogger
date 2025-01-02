#!/usr/bin/env python3
import json
import checkplayers
import sched, time
import MySQLdb as mysql
import os
import dotenv
import sys

dotenv.load_dotenv()

def log(scheduler: sched.scheduler):
    scheduler.enter(900 - (time.time() % 900), 1, log, (scheduler,))
    sql = mysql.connect("localhost", "nf-monitor", os.getenv("SQLPASS"), "nf-monitor")
    # sql.query(f"INSERT INTO PlayerCount (Time, PlayerCount) VALUE (NOW(), 0);")
    count = checkplayers.checkplayers('noob-friendly.com')
    print(count)
    sql.query(f"INSERT INTO `PlayerCount` (`Time`, `PlayerCount`) VALUE (NOW(), {count});")
    sql.commit()
    
if __name__ == "__main__":
    logger = sched.scheduler(time.time, time.sleep)
    logger.enter(0 if "debug" in sys.argv else 900 - (time.time() % 900), 1, log, (logger,))
    logger.run()
