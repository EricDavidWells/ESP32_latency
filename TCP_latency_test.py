# https://techtutorialsx.com/2018/05/17/esp32-arduino-sending-data-with-socket-client/
import select
import socket
import time

filename = r"data\TCP_latency_test_60s_1m.txt"
rec_len = 16    # amount of bytes to receive
test_len = 60   # length of time to test latency for
port = 8090  # set port for socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
esp32_ip = '192.168.4.1'    # set ip address of esp32 access point
s.connect((esp32_ip, port))

s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1) # turn off nagles algorithm
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.setblocking(False)    # turn off blocking
timeout = 0.00001   # set timeout for checking if bytes have been receieved

s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, rec_len) # adjust socket receive buffer length to match size of data packet

f = open(filename, "w")

# wait for single transmission to start test
startflag = False
while not startflag:
    startflag = select.select([s], [], [], timeout)[0]

s.recv(rec_len)
start_time = time.perf_counter()
last_time = start_time
while time.perf_counter() < start_time + test_len:

    ready = select.select([s], [], [], timeout)
    if ready[0]:
        message = s.recv(rec_len)
        read_time = time.perf_counter()

        f.write("{:2.5f}\n".format(read_time-last_time))
        last_time = read_time

f.close()
