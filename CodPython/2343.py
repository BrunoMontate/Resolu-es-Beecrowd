qtd_teste = int(input())
for i in range(qtd_teste):
    soma = 0
    localizacao_raio = []
    raio_atual = input()
    if raio_atual in localizacao_raio == False:
        localizacao_raio.append(raio_atual)
    elif raio_atual in localizacao_raio == True:
        soma = soma + 1
if soma == 0:
    print('0')
else:
    print('1')

