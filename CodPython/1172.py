#subprogramacao
def conversao(vals):
    for i in range(len(vals)):
        if (vals[i] <= 0)  :
            vals[i] = 1
            print('X[{}] = {}'.format(i,vals[i]))
        else:
            print('X[{}] = {}'.format(i, vals[i]))
#programaprincial
valores = [None]*10
for i in range(len(valores)):
    valores[i] = int(input())
conversao(valores)