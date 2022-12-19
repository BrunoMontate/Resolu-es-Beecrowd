#subprogramacao
def multiplicar(val):
    for i in range(10):
        if i == 0:
            val = val * 1
            print("N[{}] = {}".format(i, val))
        else:
            val = (val) * 2
            print("N[{}] = {}".format(i,val))

#programaprincipal
valor = int(input())
multiplicar(valor)
