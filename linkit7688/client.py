import socket
import sys
import threading
import time

import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.ini')
HOST = config.get('MYSERVER', 'HOST')
PORT = int(config.get('MYSERVER', 'PORT'))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

sys.path.insert(0, '/usr/lib/python2.7/bridge/')  

from bridgeclient import BridgeClient as bridgeclient
value = bridgeclient()

h0 = ""

def pipe_form_arduino():
	while True:
		global h0
		h0 = value.get("msg")
		if h0 == None:
			h0 = "empty" 

def send_to_server():
	while True:
		global h0
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOST, PORT))
		client.send(str(h0))
		time.sleep(1)

t1 = threading.Thread(target = pipe_form_arduino)
t2 = threading.Thread(target = send_to_server)

t1.start()
t2.start()

t1.join()
t2.join()
