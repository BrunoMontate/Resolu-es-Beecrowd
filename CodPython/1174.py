#subprograma
def apenasMenorDez(lista):
    for i in range(len(lista)):
        if lista[i] <= 10:
            print("A[{}] = {}".format(i, lista[i]))
#programaprincipal
max = 100
while max > 0:
    lista = []
    for valor in range(max):
        lista.append(float(input()))
        max = max - 1
apenasMenorDez(lista)