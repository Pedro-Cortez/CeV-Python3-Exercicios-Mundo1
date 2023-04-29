#Análise de nome próprio
nome = str(input('Digite seu nome completo: ')).strip()

#Análise
nomediv = nome.split()

#Resposta
print('Seu primeiro nome é {}{}{}.'.format('\033[4;33m', nomediv[0], '\033[m'))
print('Seu último nome é {}{}{}.'.format('\033[4;33m', nomediv[-1], '\033[m'))

#Gabarito
print('{}Seu último nome é {}.{}'.format('\033[1;31m', nomediv[len(nomediv)-1], '\033[m'))
