tabuleiro = []
linha = []
num_linha = int(input())
num_col = int(input())
casa = ""
for i in range(1,num_linha):
    linha.append([])
    for c in range(1,num_col):
        if c % 2 == 0:
            #casa == 0
            linha.append('0')
            tabuleiro.append(linha)
    print(tabuleiro[num_linha -1][num_col -1])


