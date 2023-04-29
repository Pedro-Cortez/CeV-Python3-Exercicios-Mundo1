print('\033[35m-=-' * 11)
print('\tAnalisador de Triângulos')
print('-=-' * 11, '\033[m')
a = float(input('Primeiro segmento de reta (cm): '))
b = float(input('Segundo segmento de reta (cm): '))
c = float(input('Terceiro segmento de reta (cm): '))

#Análise
if a + b > c and a + c > b and b + c > a:
    print('\n{}Esses segmentos de reta podem formar um triângulo.{}'.format('\033[1;35m', '\033[m'))
else:
    print('\n{}Esses segmentos de reta não podem formar um triângulo.{}'.format('\033[1;31m', '\033[m'))
