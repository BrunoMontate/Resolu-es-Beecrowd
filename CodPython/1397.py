def conta_casos(qtd,num_teste):
    primeira_pessoa = 0
    segunda_pessoa = 0
    for i in range(qtd):
        p1, p2 = list(map(int, input().split()))
        if p1 > p2:
            primeira_pessoa += 1
        if p1 < p2:
            segunda_pessoa += 1
    print('Teste {}'.format(num_teste))
    print(primeira_pessoa,segunda_pessoa)
    return None
#receber testes até a variavel numero de testes não for 0
primeira_pessoa = 0
segunda_pessoa= 0
num_teste = 0
qtd_teste = int(input())
while qtd_teste != 0 :
    num_teste +=1
    conta_casos(qtd_teste,num_teste)
    qtd_teste = int(input())

#repetição para receber os casos
#processr os casos
#mostrar o placar