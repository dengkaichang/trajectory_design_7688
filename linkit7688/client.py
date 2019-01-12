import socket

import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.ini')
HOST = config.get('MYSERVER', 'HOST')
PORT = int(config.get('MYSERVER', 'PORT'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = client.recv(4096)
print response