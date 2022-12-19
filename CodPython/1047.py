hora = input().split()
hi = int(hora[0])
mi = int(hora[1])
hf = int(hora[2])
mf = int(hora[3])

horaTotal = hf - hi
minTotal  = mf - mi
if (horaTotal ):
    horaTotal = 24
if (horaTotal <= 24) and (minTotal <= 59):
 print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horaTotal,minTotal))
else:
 print('')
