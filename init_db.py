#!/usr/bin/env python3
from conf4ini import Config
import shlex, subprocess

conf = Config()["Sql"]

p1 = subprocess.Popen(shlex.split("mysql"), stdin=subprocess.PIPE)
q1 = b"CREATE DATABASE `" + bytes(conf['database'], encoding='ascii') + b"`;\n"
q2 = b"CREATE USER '" + bytes(conf['username'], encoding='ascii') + b"'@'localhost';\n"
p1.communicate(b''.join((q1,q2)))

p2 = subprocess.Popen(shlex.split(f"mysql {conf['database']}"), stdin=subprocess.PIPE)
q3 = b"CREATE TABLE `PlayerCount` (\n\tTime timestamp,\n\tPlayerCount int\n);\n"
q4 = b"GRANT SELECT, INSERT ON `PlayerCount` TO '" + bytes(conf['username'], encoding='ascii') + b"'@'localhost';\n"
p2.communicate(b''.join((q3,q4)))