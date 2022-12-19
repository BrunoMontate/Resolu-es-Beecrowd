#subprograma
def calcula(termo):
    lista = [0,1]
    for i in range(2,termo+1):
        lista.append(lista[i-1]+lista[i-2])
    print("Fib({}) = {}".format(termo,lista[termo]))
    return None
nTeste = int(input())
while nTeste > 0:
    nTermo = int(input())
    calcula(nTermo)
    nTeste -= 1