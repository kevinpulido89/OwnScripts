from pubnub import Pubnub
import time
from random import randint

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f', uuid='RasPI')

my_channel = 'Temp'

def log(K):
    file = open('T.txt','a')
    file.write(str(K))
    file.write('\n')
    file.close()

#Publish Function
def loop():
    while True:
        number = randint(0,255)
        pubnub.publish(my_channel,number)
        print (number)
        log(number)
        time.sleep(2)

def destroy():
    pubnub.unsubscribe(my_channel)
    print("DISCONNECTED")

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
