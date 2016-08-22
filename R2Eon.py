from pubnub import Pubnub
import Adafruit_DHT as dht

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c',
subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f',uuid = 'PI')
channel = 'temp_humid'

#published in this fashion to comply with Eon
def loop(GPIO_pin):
    while True:
        h,t = dht.read_retry(dht.DHT11, GPIO_pin)
        #print ('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
        print([h,t])
        pubnub.publish(channel, {
            "eon":{"Temperatura":t,"Humedad":h}})

def destroy():
    print("Goodbye")

if __name__ == "__main__":
    try:
        loop(27)
    except KeyboardInterrupt:
        destroy()