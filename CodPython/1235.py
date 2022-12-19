#subprogramaçao
def semcritografia():
    frase = str(input())
    metade = int(len(frase)/2)-1
    saidaInvertida = frase[metade::-1] + frase[len(frase)-1:metade:-1]
    print(saidaInvertida)
#programaprincipal
nTeste = int(input())
while nTeste > 0:
    semcritografia()
    nTeste = nTeste - 1