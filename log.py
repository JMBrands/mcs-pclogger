#!/usr/bin/env python3
import json
import checkplayers
import sched, time

def log(scheduler: sched.scheduler):
    scheduler.enter(3600, 1, log, (scheduler,))
    data: dict
    with open("data.json", 'r') as f:
        data = json.load(f)
    data["data"].append({"time": time.time(), "players": checkplayers.checkplayers("noob-friendly.com")})
    
    with open("data.json", 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    logger = sched.scheduler(time.time, time.sleep)
    logger.enter(0, 1, log, (logger,))
    logger.run()
