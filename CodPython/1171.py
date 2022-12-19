#subprogramacao
def frequencia(lista):
    listaConvertida = sorted(set(lista))#organizar em ordem crescente e limitar a repetiçao de frases
    for i in range(len(listaConvertida)):
        if lista.count(lista[i]) != 0:
            print('{} aparece {} vez(es)'.format(listaConvertida[i],lista.count(listaConvertida[i])))

#programaprincipal
nTeste = int(input())
while nTeste > 0:
    lista = []
    for valor in range(nTeste):
        lista.append(int(input()))
        nTeste = nTeste - 1
frequencia(lista)