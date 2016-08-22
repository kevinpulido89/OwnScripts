import sys
import smbus
import time
from pubnub import Pubnub
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x12

pubnub = Pubnub(publish_key='pub-c-cbfee07b-226d-46a2-a4e4-18827eb2552c', subscribe_key='sub-c-12b25da4-5597-11e6-a5a4-0619f8945a4f')
channel = 'R2A'

def readI2Cdata(n):
        i=0
        a=[]
        while i<n:
            x=bus.read_byte_data(address,i)
            a.insert(i,x)
            i +=1
        return (a)

def main():
        array = readI2Cdata(3)
        k = (array[0] + array[1]*256)/100
        d = array[2]
        array = [k,d]
        data = {'username':'k','message':d}
        pubnub.publish(channel, data)
        print(d)

def callback(m):
  print(m)

#start process
if __name__ == '__main__':
        main()
