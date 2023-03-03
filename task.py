from celery import Celery
import json
import subprocess
import socket
from mcstatus import JavaServer
import pymongo

ip_address = socket.gethostbyname(hostname)
app = Celery('myapp', broker='pyamqp://guest@localhost//')
client = pymongo.MongoClient(f"{ip_adress}:27017")
if client.server_info():
    print("Connected to MongoDB successfully!")
else:
    print("Could not connect to MongoDB.")
db = client["treffer"]
collection = db["ips"]

@app.task
def mc_and_check_task(ip):
    host = JavaServer.lookup(ip)
    try:
        status = host.status().raw
        mc_status = {"ip": str(ip), "status": status}
        mc_status_json = json.dumps(mc_status)
        x = collection.insert_one(json.loads(mc_status_json))
        print(x)
        print(mc_status)
   # except socket.timeout:
       # print("Fehler socket.timeout")
    except TimeoutError:
        print("Fehler TimeoutError")
    except ConnectionResetError:
        print("Fehler ConnectionResetError")
    except BrokenPipeError:
        print("Fehler BrokenPipeError")
    except Exception as e:
        print(f"An error occurred: + {e}")
