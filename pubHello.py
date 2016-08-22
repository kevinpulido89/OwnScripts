import sys
from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')

channel = 'hello-pi'
w=[9,12,15]

data = {
  'username': 'Kevin Pulido' + str(1),
  #'message': 'Hello World from Pi!'
  'message': w
}

def callback(m):
  print(m)

pubnub.publish(channel, data, callback=callback, error=callback)
