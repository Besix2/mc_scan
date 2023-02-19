import json
import masscan
import pymongo
from ipranges import range_8_16
from colorama import Fore, init
from task import mc_and_check_task
#-------------------------
init()
red = Fore.RED
white = Fore.WHITE
#-------------------------
client = pymongo.MongoClient("192.168.188.32:27017")
if client.server_info():
    print("Connected to MongoDB successfully!")
else:
    print("Could not connect to MongoDB.")
db = client["treffer"]
collection = db["ips"]
#-------------------------
CIDR = 16
exclude = list()
f = open("exclude.txt", "r") 
for i in f:
   exclude.append(i.rstrip('\n'))
f.close()
while CIDR >= 8:
    IP_ranges = range_8_16(CIDR)
    IP_ranges = [x for x in IP_ranges if x not in exclude]
    for ip_range in IP_ranges:
        print(ip_range)
        try:
            mas = masscan.PortScanner()
            mas.scan(ip_range, ports="25565", arguments="--max-rate 100000")
            x = json.loads(mas.scan_result)
            len_result = len(x["scan"])
            print(len_result)
            if len_result > 0:
                print(f"Results: {red}{len_result}{white} ")
                for ip in x["scan"]:
                    adresse = ip + ":" + "25565"
                    mc_and_check_task.delay(adresse)
            else:
                print(f"Results: {white}{len_result}")

        except masscan.NetworkConnectionError:
            print(f"{ip_range}masscan connection error")
        print("done scanning")
    print(f"CIDR range {red}{CIDR}{white}scanned")
    CIDR -= 1
