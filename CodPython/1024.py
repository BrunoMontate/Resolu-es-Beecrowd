#subprograma
def priPassada():
    palavra = str(input())
    palavraCrip = ""
    chave = 3
    for letra in (palavra):
        novaLetra = ord(letra)
        if novaLetra > 64 and novaLetra < 91 or novaLetra > 96  and novaLetra < 123 :
            palavraCrip += chr(novaLetra + 3)
        else:
            palavraCrip += chr(novaLetra)
    return palavraCrip

def segPassada(palavraCrip):
    invertido = palavraCrip[::-1]
    return invertido

def terPassada(invertido):
    palavraCrip = ""
    metade = int(len(invertido) / 2)
    if len(invertido) / metade == 1:
        metade = metade + 1
    metadeInicio = invertido[0:metade]
    metadeFim = invertido[metade::]
    for letra in (metadeFim):
        novaLetra = ord(letra)
        palavraCrip += chr(novaLetra - 1)
    textofinal = metadeInicio + palavraCrip
    return textofinal

#programa principal
nTeste = int(input())
while nTeste > 0:
    resultado = terPassada(segPassada(priPassada()))
    print(resultado)
    nTeste = nTeste - 1