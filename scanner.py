import json
import masscan
import socket
import random
import pymongo
from colorama import Fore,init
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

A = list(range(1,255))
B = list(range(1,255))
random.shuffle(A)
random.shuffle(B)
#-------------------------
ip_ranges = []
for a in A:
    for b in B:
        ip_range = f"{a}.{b}.0.0/16"
        ip_ranges.append(ip_range)
#-------------------------
for ip_range in ip_ranges:
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
