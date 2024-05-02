## Scenario
Given a log file containing timestamped entries of network connections:
- Extract all unique destination IP addresses
- Print all connections that contain http/ssl traffic over non-standard ports, also change the timestamp from unix epoch to a human readable format
  
## Concepts
Malicious pcap samples: <a href="https://www.malware-traffic-analysis.net/">Malware Traffic Analysis</a>
<br><br>
<strong>Replay a pcap file to generate zeek logs</strong>:<br> `zeek -Cr sample.pcap -e 'redef LogAscii::use_json=T;'`
## Python
json loads & dumps
- `json.loads()` - Used to parse a JSON string and convert it into a Python object.
- `json.dumps()` - Used to serialize a Python object into a JSON formatted string and write it to a file-like object.

Unix epoch conversion
- `import datetime`
- `datetime.datetime.fromtimestamp(log_line["ts"]).strftime('%Y-%m-%d %H:%M:%S')`
