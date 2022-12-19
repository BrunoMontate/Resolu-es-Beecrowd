#subprograma
def receberValores():
    for i in range(14):
        valor = int(input())
    return valor
def processa(valor):
    pares = []*5
    impares = []*5
    for i in range(valor):
        if i % 2 ==0:
            pares.append(valor[i])
            print("par[{}] = {}".format(pares[i],i))
        if pares[i] == pares[4]:
            pares.clear()
        elif i % 2 != 0 :
            if impares[i] == impares[4]:
                impares.clear()
            impares.append(i)
            print("impar[{}] = {}".format(impares[i],i))

#programaprincipal
processa(receberValores())