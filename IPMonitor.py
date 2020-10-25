#version 1

import socket
import time
import datetime

ini_file = 'hosts.ini'

print("---IP Port Monitor Started---\n")

port = 22

def time_now():
    time_is = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    return time_is

def check_up():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((host, port))
    s.close()
    return result

while True:
    with open(ini_file) as hosts:
        for host in hosts:
            host = host.strip()
            if check_up():
                print(str(time_now()) + str(host) + ":" + str(port) + " looks down")
            else:
                pass
                #print(str(time_now()) + str(host) + ":" + str(port) + " looks up")
    print("\n")
    time.sleep(1)