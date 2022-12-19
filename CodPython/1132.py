n1 = int(input())
n2 = int(input())
soma = 0
if n1 > n2:
    nMaior = n1
    nMenor = n2
if n1 <= n2 :
    nMaior = n2
    nMenor = n1

while nMaior >= nMenor:
     if nMenor % 13 != 0:
         soma = soma + nMenor
     nMenor = nMenor + 1
print(soma)