## Scenario
Given a log file containing timestamped entries of network connections:
- Extract all unique destination IP addresses
- Print all connections that contain http/ssl traffic over non-standard ports, also change the timestamp from unix epoch to a human readable date format
  
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
