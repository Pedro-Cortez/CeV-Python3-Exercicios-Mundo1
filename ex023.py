#Analisador de números
number = int(input('Informe um número de 0 a 9999: '))

#Cálculo da análise
uni = number // 1 % 10
dez = number // 10 % 10
cent = number // 100 % 10
milh = number // 1000 % 10

#Análise da entrada
print('\033[35m=+=' * 10)
print('Analisando o número {}:'.format(number))
print('=+=' * 10)
print('\033[mUnidade: \033[34m{}\033[m'.format(uni))
print('Dezena: \033[34m{}\033[m'.format(dez))
print('Centena: \033[34m{}\033[m'.format(cent))
print('Milhar: \033[34m{}\033[m'.format(milh))
