# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/
import select
import socket
import time
import numpy as np

port = 8090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
esp32_ip = '192.168.4.1'
esp32_port = port
s.connect((esp32_ip, port))
s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

s.setblocking(False)    # turn off blocking
timeout = 0.00001   # set timeout for checking if bytes have been receieved
rec_len = 16    # amount of bytes to receive
test_len = 100   # length of time to test latency for


filename = "TCP_throughput_test_100s_5m.txt"
f = open(filename, "w")
start_time = time.perf_counter()
lat_time_start = start_time
while time.perf_counter() < start_time + test_len:

    ready = select.select([s], [], [], timeout)
    if ready[0]:
        # (message, address) = s.recvfrom(rec_len)
        message = s.recv(rec_len)
        read_time = time.perf_counter()

        f.write(str(read_time-lat_time_start) + ",")
        # print(address, message, message.hex())
        lat_time_start = read_time

f.close()