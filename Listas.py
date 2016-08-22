#http://www.pythondiario.com/2016/07/estructura-de-datos-listas-en-python.html

import random

n=0
for i in range(0,10):
    n += i
print(n)

palabras = ["hola", "python", "pythondiario", "hola", "python"]
for i in (palabras):
    print (i)

lista=[random.randint(10,20) for i in range(15)]
#a=[palabras.remove(hola) for i in range(5)]
print(lista)

b=palabras.pop(1)
print(b)
print(palabras)

x=[1,2,3,4,5]
print(sum(x))

#ITERANDO POR ELEMENTO
listaX=["Adameo","Mateo",14.56,False,0.789,34,"Melissa"]
for i in listaX:
    print(i)
print("Lista: ",listaX)
#ITERANDO POR ÍNDICE
for i in range(len(listaX)):
    print("Posición",i,"contiene",listaX[i])

w=[5,4,3,2,1,0]
print(w[0],w[w[0]],w[w[-1]],w[w[w[w[2]+1]]])
