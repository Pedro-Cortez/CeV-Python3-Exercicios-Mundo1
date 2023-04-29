#Média Escolar
nota1 = float(input('Informe a nota do 1º mês: '))
nota2 = float(input('Informe a nota do 2º mês: '))

#Cálculo da média bimestral
media = (nota1 + nota2)/2

#Resposta
print('A média bimestral do aluno é {}{:.2f}{}.'.format('\033[4;32m', media, '\033[m'))
