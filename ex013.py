#Aumento de salário
salario = float(input('\033[1;34mInforme o salário do colaborador: R$ \033[m'))

#Cálculo do aumento
aumento = salario + salario * (15 / 100)

#Resposta
print('\033[4;32mO novo salário do colaborador, com 15% de aumento, será R$ {:.2f}.'.format(aumento))