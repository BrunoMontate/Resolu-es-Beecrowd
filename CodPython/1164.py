controle=int(input())
for i in range(controle):
    soma=0
    num=int(input())
    for inicio in range(1,num):
        if(num%inicio==0):
            soma=soma+inicio
            #print(t)
    if (soma==num):
        print(num,"eh perfeito")
    else:
        print(num,"nao eh perfeito")


