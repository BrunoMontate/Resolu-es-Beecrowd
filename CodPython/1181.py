def geraMatriz(matriz):
    for i in range(12):
        matriz.append([])
        for l in range(12):
            valor = float(input())
            matriz[i].append(valor)
    return matriz
def somar(linha, matriz):
    soma = 0.0
    for i in range(12):
        for c in range(12):
            if i == linha:
                soma += matriz[i][c]
    return soma
def processa(resultado, oper):
    if oper == "S":
        print('{:.1f}'.format(resultado))
    elif oper == "M":
        print('{:.1f}'.format(resultado / 12))
    return None
# programaprincipal
matrizGeral = []
linhaEscolhida = int(input())
operacao = str(input())
processa(somar(linhaEscolhida, geraMatriz(matrizGeral)), operacao)