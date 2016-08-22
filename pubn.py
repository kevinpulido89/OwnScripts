from Pubnub import Pubnub
from IoT_wrapper import iotwrapper

pi = iotwrapper(publish_key = 'pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', 
		subscribe_key = 'sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f', 
		uuid = 'PI')

channel = 'iotchannel'
message = "hello from pi"

def callbackfn(m, n):
	print(m)
	
pi.send(channel, message)
		
pi.connect(channel, callbackfn)
