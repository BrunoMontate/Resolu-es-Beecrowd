entradas = input().split()
n1 = int(entradas[0])
n2 = int(entradas[1])
n3 = int(entradas[2])

maiorAB= (n1+n2+abs(n1-n2))/2
if maiorAB >n3:
    print('{:.0f} eh o maior'.format(maiorAB))
else:
    print('{:.0f} eh o maior'.format(n3))