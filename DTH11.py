#!/usr/bin/env python

import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
from pubnub import Pubnub

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')
channel = 'R2Pubnub'

Sensor = 11 #Sensor DTH11
humiture = 27 #GPIO 27

def setup():
    print('Setting up,  please wait...')

def loop():
    while True:
        humidity, temperature = DHT.read_retry(Sensor, humiture)
        array=[humidity,temperature]
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
            #data = {'username':'RPi','message':temperature}
            pubnub.publish(channel, [temperature,humidity])
        else:
            print('Failed to get reading. Try again!')

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()