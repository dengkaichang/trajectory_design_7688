import socket
import threading
import serial
import time

import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('config.ini')
HOST = config.get('MYSERVER', 'HOST')
PORT = int(config.get('MYSERVER', 'PORT'))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

s = None

def setup():
    global s
    s = serial.Serial("/dev/ttyS0", 57600)
    print("Start")
h0 = "" 
data = []
b = ''
#def loop():
    #h0 = s.read()
    #s.write("1")
    #time.sleep(1)
    #s.write("0")
    #time.sleep(1)

if __name__ == '__main__':
    setup()
    #while True:
        #loop()
def pipe_form_arduino():
    while True:
        global h0
        global data
        global b
        h0 = s.read()
        data.append(h0)
        a = ''
        b = a.join(data)
        if h0 == None:
            h0 = "empty"

def send_to_server():
    while True:
        global b
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        client.send(str(b))
        time.sleep(1)

t1 = threading.Thread(target = pipe_form_arduino)
t2 = threading.Thread(target = send_to_server)

t1.start()
t2.start()

t1.join()
t2.join()