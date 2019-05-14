import serial
import time

s = None
def setup():
	global s
	s=serial.Serial("/dev/ttys0", 9600)

def loop():
	h0 = s.read()
	print("msg: "+ str(h0))