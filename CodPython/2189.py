#receber numero de pessoas na festa
numero_convidados = int(input())
num_teste = 0
#enquanto o numero de participantes for maior que 0
while numero_convidados != 0:
    # receber numero dos participantes
    ordem_convidados = list(map(int,input().split()))
    for i in ordem_convidados:
        if i + 1  == ordem_convidados[i]:
            num_teste += 1
            print('Teste {}'.format(num_teste))
            print(ordem_convidados[i])
            print()
#acrescenta um teste
#processar
#mostrar o resultado