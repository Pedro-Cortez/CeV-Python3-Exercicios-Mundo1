#Sorteio aleatório de alunos
import random

aluno1 = str(input('\033[34mPrimeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: \033[m'))

#Outra forma de sorteio
lista = [aluno1, aluno2, aluno3, aluno4]
escolha = random.choice(lista)

#Resultado
print('O aluno sorteado foi \033[31m{}\033[m.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))

#Gabarito
print('\nO aluno escolhido foi \033[31m{}\033[m'.format(escolha))
