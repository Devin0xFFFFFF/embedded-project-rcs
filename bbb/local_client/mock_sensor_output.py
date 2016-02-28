
import time
import datetime
import socket
import random

IP = "127.0.0.1"
PORT = 5632

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


n = 0
pressed = False

while True:

    currentTime = str(datetime.datetime.now())
    INPUT = random.randint(1,100)
    msg = "fake random number: {0} @ {1}". format(INPUT, currentTime)
    sock.sendto(msg.encode('utf-8'), (IP, PORT))
    time.sleep(1)
    print('fake local server running: {0}'.format(INPUT))
