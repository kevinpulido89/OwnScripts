from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-0fcd5ed3-8d87-43e5-a3e5-285a0b450a6d", subscribe_key="sub-c-00081af4-5597-11e6-bd9c-0619f8945a4f")
def callback(message, channel):
    print(message)
  
  
def error(message):
    print("ERROR : " + str(message))
  
  
def connect(message):
    print("CONNECTED")
    print pubnub.publish(channel='Channelpy', message='Hello from the PubNub Python SDK')
  
  
def reconnect(message):
    print("RECONNECTED")
  
  
def disconnect(message):
    print("DISCONNECTED")
  
  
pubnub.subscribe(channels='Channelpy', callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)
