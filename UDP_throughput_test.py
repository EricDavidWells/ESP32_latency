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

bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
print("Default socket receive buffer size: " + str(bufsize))
# bufsize_new = 16*10
# s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, bufsize_new)

start_time = time.perf_counter()
lat_time_start = start_time
latency = np.array([])
filename = "2020-07-27_UDP_throughput_test_100s_16buf.txt"
f = open(filename, "w")
while time.perf_counter() < start_time + test_len:
    # if data has been sent, read a single byte of it
    ready = select.select([s], [], [], timeout)
    if ready[0]:
        (message, address) = s.recvfrom(rec_len)
        read_time = time.perf_counter()
        f.write(str(read_time-lat_time_start) + ",")
        print(int.from_bytes(message[0:8], byteorder='little', signed=False))

        lat_time_start = read_time

f.close()