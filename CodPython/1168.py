
def contarLed():
    valor = input()
    qtdLed = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
    totalLed = 0
    for v in valor:
        totalLed += qtdLed[int(v)]
    print("%d leds" % int(totalLed))
#programaprincipal
nTeste = int(input())
while nTeste > 0:
    contarLed()
    nTeste -=1