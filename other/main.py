import serial
import time

s = None
data = []
def setup():
	global s
	global data
	s = serial.Serial("/dev/ttyS0", 57600)
	print("Start")

def loop():
	#print(s.read())
	h0 = s.read()
	data.append(h0)
	a = ''
	print a.join(data)
	#s.write("1")
	#time.sleep(1)
	#s.write("0")
	#time.sleep(1)

if __name__ == '__main__':
	setup()
	while True:
		loop()