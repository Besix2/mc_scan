import json
from celery import Celery
import masscan
import subprocess
from ipranges import range_8_16
from colorama import Fore, init
from task import mc_and_check_task
import time
#-------------------------------------------------------------------------------------
init()
red = Fore.RED
white = Fore.WHITE
#-------------------------------------------------------------------------------------
subprocess.Popen(['celery', '-A', 'task', 'worker', '--loglevel=WARNING', "--uid=pi"])
time.sleep(2)
CIDR = 16
exclude = list()
with open("exclude.txt", "r") as exclude_1:
    for i in exclude_1:
        exclude.append(i.rstrip('\n'))
#-------------------------------------------------------------------------------------
while CIDR >= 8:
    with open("config.txt","r") as config:
        lines = config.readlines()
        l1 = lines[0].strip()
        l2 = int(lines[1].strip())
#-------------------------------------------------------------------------------------
    CIDR = l1.split("/")
    IP_ranges = range_8_16(int(CIDR[1]))
    IP_ranges = [x for x in IP_ranges if x not in exclude]
    index = IP_ranges.index(l1)
    IP_ranges = IP_ranges[index+1:]
#-------------------------------------------------------------------------------------
    for ip_range in IP_ranges:
        print(ip_range)
        try:
            mas = masscan.PortScanner()
            mas.scan(ip_range, ports="25565", arguments=f"--max-rate {l2} --wait 3")
            x = json.loads(mas.scan_result)
            len_result = len(x["scan"])
#-------------------------------------------------------------------------------------
            if len_result > 0:
                print(f"Results: {red}{len_result}{white} ")
                for ip in x["scan"]:
                    adresse = ip + ":" + "25565"
                    mc_and_check_task.delay(adresse)
            else:
                print(f"Results: {white}{len_result}")
#-------------------------------------------------------------------------------------
        except masscan.NetworkConnectionError:
            print(f"{ip_range}masscan connection error")
        print("done scanning")
        lines[0] = f"{ip_range}\n"
#-------------------------------------------------------------------------------------
        with open("config.txt", "w") as f:
            f.writelines(lines)
    print(f"CIDR range {red}{CIDR}{white}scanned")
    CIDR -= 1
