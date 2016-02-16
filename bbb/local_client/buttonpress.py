import Adafruit_BBIO.GPIO as GPIO
import time
import datetime
import socket

IP = "127.0.0.1"
PORT = 5632

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

GPIO.setup("P8_12", GPIO.IN, GPIO.PUD_UP)
n = 0
pressed = False

while True:

    currentTime = str(datetime.datetime.now())
    INPUT = GPIO.input("P8_12")
    if INPUT:

        if not pressed:
            pressed = True
            n = n + 1
            MSG_DOWN = "Button Down: {0} @ {1}".format(n, currentTime)
            sock.sendto(MSG_DOWN.encode('utf-8'), (IP, PORT))
        else:
            time.sleep(0.1)
    elif pressed:
        pressed = False
        MSG_UP = "Button Up: {0} @ {1}".format(n, currentTime)
        sock.sendto(MSG_UP.encode('utf-8'), (IP, PORT))
