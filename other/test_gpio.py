import mraa
import time
 
WAY = mraa.Gpio(43)	#GPIO43 on 7688
WAY.dir(mraa.DIR_IN)

OUT_FLAG = 1

while True:
	print("read:" + str(WAY.read()))

