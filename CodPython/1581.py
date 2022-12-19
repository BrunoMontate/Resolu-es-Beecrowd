#subprograma
def selecaoIdioma():
    idioma = []
    nPessoas = int(input())
    while nPessoas > 0:
        idioma.append( str(input()))
        nPessoas = nPessoas -1
    controle = idioma[0]
    for npessoas in idioma:
        if npessoas != controle:
            controle = 'ingles'
    #return print(controle)
    return controle
#programa principal
nTeste = int(input())
while nTeste > 0:
    resultado = selecaoIdioma()
    print(resultado)
    nTeste = nTeste - 1

