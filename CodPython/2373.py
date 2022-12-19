rodadas = int(input())
copos_quebrados = 0
for i in range(rodadas):
    bandeja = list(map(int,input().split()))
    if bandeja[0] > bandeja[1]:
        copos_quebrados = copos_quebrados + bandeja[1]
print(copos_quebrados)