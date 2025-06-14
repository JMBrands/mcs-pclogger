#!/usr/bin/env python3
import json
import checkplayers
import sched, time
import MySQLdb as mysql
import os
import sys
from conf4ini import Config


def log(scheduler: sched.scheduler, sqls: dict, mains: dict):
    if "once" not in sys.argv:
        scheduler.enter(mains["interval"], 1, log, (scheduler, sqls, mains))
    sql = mysql.connect(sqls["hostname"], sqls["username"], database=sqls["database"])
    # sql.query(f"INSERT INTO PlayerCount (Time, PlayerCount) VALUE (NOW(), 0);")
    count = checkplayers.checkplayers(mains)
    print(count)
    sql.query(f"INSERT INTO `PlayerCount` (`Time`, `PlayerCount`) VALUE (NOW(), {count});")
    sql.commit()
    
if __name__ == "__main__":
    config: Config
    try:
        config = Config("..")
    except FileNotFoundError:
        config = Config()
    
    sqls = config["Sql"]
    mains = config["Main"]
    logger = sched.scheduler(time.time, time.sleep)
    logger.enter(0, 1, log, (logger, sqls, mains))
    logger.run()
