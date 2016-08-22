import smbus
import time
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x12
d=0

# Definicion de funciones
def writeNumber(x,y):
        value = [];
        value.append(x);
        value.append(y);
        bus.write_block_data(address, 0, value)
        return -1

def readI2Cdata(n):
        i=0
        a=[]
        while i<n:
            x=bus.read_byte_data(address,i)
            a.insert(i,x)
            i +=1
        return (a)

# Script que usa las funciones definidas
#var1 = int(input("Enter number : "))
#var2 = int(input("Enter number : "))
#writeNumber(var1,var2)
#print ('RPI: Hi Arduino, I sent you ' + str(var1)+ " & " + str(var2))

# sleep one second
#time.sleep(1)

while d<=12:
	array = readI2Cdata(3)

	k = (array[0] + array[1]*256)/100
	print ("El voltaje es: " + str(k) +"v")

	d = array[2]
	print ("La distancia es: " + str(d) + "cm")

	array = [k,d]
	print (array)
	
	time.sleep(2.68)

print ("Salimos!")
