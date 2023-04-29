#Módulo descoberta da hipotenusa
from math import hypot

cateto_op = float(input('\033[33mInforme comprimento do cateto oposto: '))
cateto_ad = float(input('Informe comprimento do cateto adjacente: \033[m'))
print('\033[34mA hipotenusa mede {:.2f}.\033[m'.format(hypot(cateto_op, cateto_ad)))

#Cálculo prova real
hipot = (cateto_op ** 2 + cateto_ad ** 2) ** (1/2)
print('\033[31m\n\nProva Real: {:.2f}\033[m'.format(hipot))
