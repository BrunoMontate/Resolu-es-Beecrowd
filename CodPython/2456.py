#receber dados na mesma linha
cartas = list(map(int,input().split()))
if cartas[0] < cartas[1] and cartas[1] < cartas[2] and cartas[2] < cartas[3] and cartas[3] < cartas[4]:
    print('C')
elif cartas[0] > cartas[1] and cartas[1] > cartas[2] and cartas[2] > cartas[3] and cartas[3] > cartas[4]:
    print('D')
else:
    print('N')
#processar os casos
# for entre os elementos
# se n1 < n2 and n2....
#se n1 > n2 and...
#mostrar resultado