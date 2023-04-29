#Jogo de adivinhação
import random
from time import sleep

#Sorteio
lista = [0, 1, 2, 3, 4, 5]
escolha = random.choice(lista)

#Escolha do usuário
print('{}Adivinhe, em qual número estou pensado?\n'.format('\033[32m'))
palpite = int(input('Escolha um número de 0 a 5: '))
print('\nPROCESSANDO...{}'.format('\033[m'))
sleep(2)
if palpite == escolha:
    print('{}Parabéns! Você acertou.{}'.format('\033[1;36m', '\033[m'))
else:
    print('{}Que pena! Pensei no número {}.\nVocê errou! Tente Novamente.{}'.format('\033[1;31m', escolha, '\033[m'))
