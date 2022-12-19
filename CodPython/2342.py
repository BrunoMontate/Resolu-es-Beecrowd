def processa():
    resultado = None
    operacao = list(map(str, input().split()))
    operacao[0] = int(operacao[0])
    operacao[2] = int(operacao[2])
    if operacao[1] == "+":
        resultado = operacao[0] + operacao[2]
    elif operacao[1] == "*":
        resultado = operacao[0] * operacao[2]

    return resultado
valor_max = int(input())
if processa() > valor_max:
    print('OVERFLOW')
else:
    print('OK')