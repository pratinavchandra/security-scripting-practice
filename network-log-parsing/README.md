## Scenario
Given a log file containing timestamped entries of network connections, write a Python function to extract all unique IP addresses that have made more than 100 connections within a 10-minute window.

Zeek Logs - <a href="https://www.secrepo.com/maccdc2012/conn.log.gz">logs</a>

## Concepts
Malicious pcap samples: <a href="https://www.malware-traffic-analysis.net/">Malware Traffic Analysis</a>
<br><br>
<strong>Replay a pcap file to generate zeek logs</strong>:<br> `zeek -Cr sample.pcap -e 'redef LogAscii::use_json=T;'`
## Python
json loads & dumps
- The json.loads() function is used to parse a JSON string and convert it into a Python object
- json.dumps() function is used to serialize a Python object into a JSON formatted string and write it to a file-like object.
  
  ```python
  import json
  file_path = "conn.log"
  data = 
  ```
