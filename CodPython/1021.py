import math
valor = float(input())
print('NOTAS:')
notas = [100,50,20,10,5,2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]
for nota in notas:
    qntnotas = int(valor / nota)
    print('{} nota(s) de R$ {:.2f}'.format(qntnotas,nota))
    valor -= qntnotas * nota
print('MOEDAS:')
for moeda in moedas:
    valor = round(valor, 2)
    qntmoedas = int(valor/moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(qntmoedas, moeda))
    valor -= qntmoedas * moeda