# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/
import select
import socket
import time
import numpy as np

port = 8090
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
esp32_ip = '192.168.4.1'
esp32_port = port

s.bind(('0.0.0.0', port))   # bind socket to no particular address, and a specific port
s.setblocking(False)    # turn off blocking
timeout = 0.0001   # set timeout for checking if bytes have been receieved
rec_len = 16    # amount of bytes to receive
test_len = 100   # length of time to test latency for

bytecounter = 0
start_time = time.perf_counter()
lat_time_start = start_time
latency = np.array([])
filename = "latency_test_.txt"
f = open(filename, "w")

while time.perf_counter() < start_time + test_len:

    returnmessage = "h"
    s.sendto(returnmessage.encode(), (esp32_ip, esp32_port))

    # if data has been sent, read a single byte of it
    ready = select.select([s], [], [], timeout)
    if ready[0]:
        (message, address) = s.recvfrom(rec_len)
        rectime = time.perf_counter()
        f.write(str(rectime-lat_time_start) + ",")
        print(address, message, message.hex())
        lat_time_start = rectime

f.close()
