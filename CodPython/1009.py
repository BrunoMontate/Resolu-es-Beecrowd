nome =str(input()) #nome
salario = float(input()) #coleta do salario
venda = float(input()) #coleta do bonus
bonus = salario + (venda*0.15)
print('TOTAL = R$ {:.2f}'.format(bonus))

