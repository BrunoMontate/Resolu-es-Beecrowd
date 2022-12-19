#subprograma
def recebe(tam):
    vetor = []*tam
    valores = list(map(int,input().split()))
    valor = ""
    for i in range(len(valores)):
        vetor.append(valores[i])
    return vetor
def processa(val):
    menorValor = val[0]
    posicao = 0
    for i in range(1,len(val)):
        if val[i] < menorValor:
            menorValor = val[i]
            posicao = i
    print("Menor valor: {}".format(menorValor))
    print('Posicao: {}'.format(posicao))

#programaprincipal
tamanhoVetor = int(input())
processa(recebe(tamanhoVetor))
