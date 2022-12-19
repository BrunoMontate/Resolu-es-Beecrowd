conceito = None
nota = int(input())
if nota == 0:
    conceito = 'E'
elif 1<= nota <= 35:
    conceito = 'D'
elif 36<= nota <= 60:
    conceito = 'C'
elif 61<= nota <= 85:
    conceito = 'B'
elif 86<= nota <= 100:
    conceito = 'A'
print(conceito)