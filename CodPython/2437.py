minimo_passo_x = 0
minimo_passo_y = 0
coordenadas = list(map(int,input().split()))
if coordenadas[0] >= coordenadas[2]:
    minimo_passo_x = coordenadas[0] - coordenadas[2]
else:
    minimo_passo_x = coordenadas[2] - coordenadas[0]
if coordenadas[1] >= coordenadas[3]:
    minimo_passo_y = coordenadas[1] - coordenadas[3]
else:
    minimo_passo_y = coordenadas[3] - coordenadas[1]
qtd_passos_finais = minimo_passo_x + minimo_passo_y
print(qtd_passos_finais)