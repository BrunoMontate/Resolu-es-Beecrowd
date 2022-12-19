D = 0
E = 0
F = 0
val_e_teste = list(map(int,input().split()))
D = val_e_teste[0]
E = val_e_teste[0]
F = val_e_teste[0]
for i in range(val_e_teste[1]):
    situação = list(map(str,input().split()))
    if situação[0] == 'C':
        situação[2] = int(situação[2])
        situação[1] -= situação[2]
    print('{}{}{}'.format(D,E,F))