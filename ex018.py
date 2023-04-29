#Módulo seno, cosseno e tangente
import math
angulo = float(input('\033[31mInforme o valor do ângulo a ser analisado: \033[m'))

#Cálculos
angrad = math.radians(angulo)
senrad = math.sin(angrad)
cosrad = math.cos(angrad)
tangrad = math.tan(angrad)


#Respostas
print('\033[34mPara o ângulo de {}º:\033[m'.format(angulo))
print('O \033[32mseno\033[m é igual a \033[32m{:.2f}\033[m.'.format(senrad))
print('O \033[33mcosseno\033[m é igual a \033[33m{:.2f}\033[m.'.format(cosrad))
print('A \033[35mtangente\033[m é igual a \033[35m{:.2f}\033[m.'.format(tangrad))
