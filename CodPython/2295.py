distancia_de_controle = 100
valores = list(map(float,input().split()))
alcool = (distancia_de_controle / valores[2]) * valores[0]
gasolina = (distancia_de_controle / valores[3]) * valores[1]
if gasolina <= alcool:
    print('G')
else:
    print('A')
