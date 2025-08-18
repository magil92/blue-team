"""my_list = []  
my_list.append(2)  
print(my_list)"""

"""for i in range(21): 
    if i % 2 == 0:  
        print(i)  """

"""for i in range(21): 
    if i % 2 != 0:  
        print(i) 
"""

"""from collections import namedtuple
from pathlib import Path  

Event = namedtuple("Event", ["ip", "risk_score"])

print(Event)

events = [
    Event("192.168.1.10", 5.0),
    Event("203.0.113.45", 9.2),
    Event("198.51.100.23", 8.7),
]

suspicious_ips = [x.ip for x in events if x.risk_score > 7.0]

print("Suspicious IPs:", suspicious_ips)


def process_evidence_line(line):
    print(f"[EVIDENCE] processing: {line.strip()}")


evidence_file = Path("evidence.log")

if evidence_file.exists():
    with evidence_file.open() as file:
        for line in file:
            process_evidence_line(line)
else:
    print("[WARNING] evidence.log not found")
"""

