#subprogramacao
def semCriptografia():
    frase = str(input()).upper()
    chave = int(input())
    fraseFinal = ''
    for letra in frase:
        novaLetra = ord(letra) - chave
        if (novaLetra < 65):
            fraseFinal += chr(91 - (65 - novaLetra ))
        else:
            fraseFinal += chr(ord(letra) - chave)
    return fraseFinal
#programa
qtdTeste = int(input())
while qtdTeste > 0:
    resultado = semCriptografia()
    print(resultado)
    qtdTeste = qtdTeste - 1