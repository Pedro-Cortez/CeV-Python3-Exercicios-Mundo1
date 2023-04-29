#Sorteio de ordem de objetos
import random

aluno1 = str(input('\033[34mPrimeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: \033[m'))

#Realização do sorteio
lista =[aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

#Resposta
print('A ordem dos alunos que apresentarão o trabalho será: \033[31m{}\033[m.'.format(lista))