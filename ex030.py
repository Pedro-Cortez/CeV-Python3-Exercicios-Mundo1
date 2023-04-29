#PAR ou ÍMPAR
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('O número {}{}{} é {}PAR{}.'.format('\033[4;31m', numero, '\033[m', '\033[1;33m', '\033[m'))
else:
    print('O número {}{}{} é {}ÍMPAR{}.'.format('\033[4;31m', numero, '\033[m', '\033[1;33m', '\033[m'))
