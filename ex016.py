#Módulo para demonstrar parte inteira de um número
from math import trunc

numero = float(input('\033[1;31mDigite um número real qualquer: \033[m'))

print('\033[33mA parte inteira do número {} corresponde a {}.\033[m'.format(numero, trunc(numero)))
print('\033[34mA parte inteira do número {} corresponde a {}.\033[m'.format(numero, int(numero)))
