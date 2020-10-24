#version 1

import socket
import time
import datetime

print("---IP Port Monitor Started---\n")

hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.188', '192.168.1.253', '192.168.1.254']
port = 80

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
    for host in hosts:
        if check_up():
            print(str(time_now()) + str(host) + ":" + str(port) + " looks down")
        else:
            #pass
            print(str(time_now()) + str(host) + ":" + str(port) + " looks up")
    print("\n")
    time.sleep(1)