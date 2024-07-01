import json
import datetime
import collections
def nonstandard_traffic(log_line):
    timestamp = datetime.datetime.fromtimestamp(log_line["ts"]).strftime('%Y-%m-%d %H:%M:%S')
    if log_line["proto"] == "tcp":
        if (log_line["service"] == "ssl" and log_line["id.resp_p"]!=443) or (log_line["service"] == "http" and log_line["id.resp_p"]!=80):
            log_line["ts"]=timestamp
            print(log_line)
file_path = "conn.log"
destips=[]
with open(file_path, 'r') as logs:
    for line in logs:
        log_line = json.loads(line)
        destips.append(log_line["id.resp_h"])
        nonstandard_traffic(log_line)
print("")
print(set(destips))
print("")
print(max(collections.Counter(destips).items()))
print("")