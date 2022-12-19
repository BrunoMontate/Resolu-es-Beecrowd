prox_carta = None
cartas = list(map(int,input().split()))
if cartas[0] == cartas[1]:
    prox_carta = cartas[0]
if cartas[0] > cartas[1]:
    prox_carta = cartas[0]
else:
    prox_carta = cartas[1]
print(prox_carta)