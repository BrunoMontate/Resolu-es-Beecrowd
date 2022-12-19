#subprogramação
def media(notas):
    resultado = (notas[0] + notas[1]) / 2
    print("media = {:.2f}".format(resultado))
#programação
limite = 0
notasValidas = []
while limite < 2:
    nota = float(input())
    if (nota >= 0) and (nota <= 10) :
        limite = limite + 1
        notasValidas.append(nota)
    else:
        print('nota invalida')
media(notasValidas)
