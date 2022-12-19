#subprogramacao
def vetorInvertido(lista):
    listaInvertida =lista[::-1]
    for i in range(len(listaInvertida)):
        print('N[{}] = {}'.format(i,listaInvertida[i]))
#programaprincipal
max = 20
while max > 0:
    lista = []
    for valor in range(max):
        lista.append(int(input()))
        max = max - 1
vetorInvertido(lista)