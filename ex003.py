# Entrada do Usuário
num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 2º valor: '))
# Cálculo de soma
soma = num1 + num2

# Resposta
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'
      .format('\033[1;31m', num1, '\033[m', '\033[1;31m', num2, '\033[m', '\033[1;36m', soma, '\033[m'))
