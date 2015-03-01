import socket
import requests
import json

IP = "127.0.0.1"
PORT = 5632

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

REMOTE_URL = "http://192.168.7.1:5000"

while True:
	data, addr = sock.recvfrom(1024)
	print(data.decode('utf-8'))
	post_data = json.dumps({'data':data.decode('utf-8')})
	r = requests.post(REMOTE_URL, post_data)
	print(r.status_code)
