import random

def leerLista():
    lista=[]
 
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 5)))
        i=i+1
    return lista

def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print (nombre + "[" + str(i) + "]=" + str(lista[i]))

def promediarLista(lista):
    sum=0.0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
 
    return sum/len(lista)
 
A=leerLista()
imprimirLista(A,"A")
print ("Promedio = " + str(promediarLista(A)))
