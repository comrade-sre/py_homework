#!/usr/bin/env python3
import re,sys
if len(sys.argv) < 2:
    print("please, define log file")
    exit(1)
log_file = sys.argv[1]
log = open(log_file, "r")
logr = log.read()
pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
result = re.findall(pattern, logr)
res_set = set(result)
finish = []
for address in res_set:
    my_tuple = (address, result.count(address))
    finish.append(my_tuple)
finish = sorted(finish, key=lambda finish: finish[1], reverse=True)
for value in finish:
    print(*value)
