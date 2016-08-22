def CrearArray():
    a=[]
    i=0
    while len(a) < 4:
        print (a)
        a.insert(i,int(input("Numero:")))
        i=i+1
	b=a
    return a,b

def PromediarArray(array):
    sum=0.0
    for i in range(0,len(array)):
        sum=sum+array[i]
    return sum/len(array)

h,t=CrearArray()
while len(t) >= 4:
    t.remove(t[0])
    t.insert(len(t),int(input("Numero:")))
    p=PromediarArray(t)
    print(p)
    if t[len(t)-1]==99:
        break
print("Exit, el último promedio fue: ", p)
print(h)