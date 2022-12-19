vInter = 0
vGremio = 0
empate = 0
tevePartida = 1
partidas = 0
maiorVencedor = 0
while tevePartida == 1:
    inter,gremio = map(int,input().split())
    partidas = partidas + 1
    if (inter > gremio):
        vInter+=1
    if (gremio > inter):
        vGremio+=1
    if (inter==gremio):
        empate+=1
    tevePartida = int(input('Novo grenal (1-sim 2-nao)\n'))
if vInter > vGremio and vInter > empate:
        maiorVencedor = 'Inter venceu mais'
if vGremio > vInter and vGremio > empate:
        maiorVencedor = 'Gremio venceu mais'
if empate > vInter and empate > vGremio:
        maiorVencedor = 'Nao houve vencedor'
if tevePartida ==2:
    print(partidas, 'grenais')
    print('Inter:{}'.format(vInter))
    print('Gremio:{}'.format(vGremio))
    print('Empates:{}'.format(empate))
    print(maiorVencedor)