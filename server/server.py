import socket
import threading

import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.ini')
HOST = config.get('MYSERVER', 'HOST')
PORT = int(config.get('MYSERVER', 'PORT'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
            
server.listen(5)
 
print "[*] Listening on %s:%d" % (HOST, PORT)
 
def handle_client(client_socket):
    
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    
    # client_socket.send("ACK!")
    client_socket.close()
    
while True:
    client, addr = server.accept()
    print "[*] Acepted connection from: %s:%d" % (addr[0],addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()