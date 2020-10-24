#version 1

import socket
import time
import datetime

print("---IP Port Monitor Started---\n")

host = '192.168.1.1'
port = 80

while True:

    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()

    if result:
        print(time_now + str(host) + ":" + str(port) + " looks down")
    else:
        print(time_now + str(host) + ":" + str(port) + " looks up")

    time.sleep(1)