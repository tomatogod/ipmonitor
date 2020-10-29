#repository https://github.com/tomatogod/ipmonitor

import socket #module for connection test
import time #module for time sleep
import datetime #module for log timestamp
import os #module to get file path

def time_now(): #function for timestamp
    time_is = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ") #format date time string
    return time_is #return 

print(str(time_now()) + "---IP Port Monitor Started---\n") #start msg to console

path = os.path.dirname(os.path.realpath(__file__)) #find path of host file
ini_file = path + "\\" + 'hosts.ini' #specify hosts.ini file
log_file_path = path + "\\" + 'results.log' #specify log output file

log_file = open(log_file_path, 'a+') #open log
log_file.write(str(time_now()) + "---IP Port Monitor Started---\n") #welcome message in log
log_file.close() #close log

port = 80 #static port to check

def check_up(): #function to use socket connect_ex to check if
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specify socket to use IPV4
    s.settimeout(1) #timeout for closed port
    s.setblocking(True)
    result = s.connect_ex((host, port))
    s.close()
    return result

while True: #logic to start a loop
    with open(ini_file) as hosts: #open ini file
        for host in hosts: #use ini as a list
            host = host.strip() #strip out new line characters
            if check_up(): #if function is true
                log_file = open(log_file_path, 'a+') #reopen log file             
                print(str(time_now()) + str(host) + ":" + str(port) + " looks down") #write to console
                log_file.write(str(time_now()) + str(host) + ":" + str(port) + " looks down\n") #write to log
                log_file.close() #close log
            else: #if function is false
                pass #skip
    time.sleep(10) #sleep timer between loops