import json
import datetime
def nonstandard_traffic(log_line):
    timestamp = datetime.datetime.fromtimestamp(log_line["ts"]).strftime('%Y-%m-%d %H:%M:%S')
    if log_line["proto"] == "tcp":
        if (log_line["service"] == "ssl" and log_line["id.resp_p"]!=443) or (log_line["service"] == "http" and log_line["id.resp_p"]!=80):
            log_line["ts"]=timestamp
            print(log_line)
file_path = "conn.log"
uniq_destips=[]
with open(file_path, 'r') as logs:
    for line in logs:
        log_line = json.loads(line)
        if log_line["id.resp_h"] not in uniq_destips:
            uniq_destips.append(log_line["id.resp_h"])
        nonstandard_traffic(log_line)
print("")
print(uniq_destips)
