import sys 

sys.path.insert(0, '/usr/lib/python2.7/bridge/')  
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

while True:  
    h0 = value.get("msg")
    print("msg: "+ str(h0))