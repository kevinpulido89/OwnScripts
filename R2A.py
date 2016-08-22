import sys
import smbus
import time
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x12

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
	print (d)
	
#start process
if __name__ == '__main__':
	main()