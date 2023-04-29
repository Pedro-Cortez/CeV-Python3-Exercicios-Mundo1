#Radar eletrônico
veloz = float(input('Velocidade aferida (km/h): '))

#Cálculo da multa
multa = (veloz - 80) * 7

#Respostas
if veloz >= 80:
    print('{}Você ultrapassou o limite de 80 km/h.'.format('\033[31m'))
    print('Deverá receber multa de {}R$ {:.2f}{}.'.format('\033[4m', multa, '\033[m'))
print('{}Dirija com segurança!{}'.format('\033[1;34m', '\033[m'))
