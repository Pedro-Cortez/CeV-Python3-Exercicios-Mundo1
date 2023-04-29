#Descobrir maior valor e menor valor
numeroA = int(input('Primeiro valor: '))
numeroB = int(input('Segundo valor: '))
numeroC = int(input('Terceiro valor: '))

#Gabarito
menor = numeroA
#Verificando menor valor
if numeroB < numeroA and numeroB < numeroC:
    menor = numeroB
if numeroC < numeroA and numeroC < numeroB:
    menor = numeroC

#Verificando maior valor
maior = numeroA
if numeroB > numeroA and numeroB > numeroC:
    maior = numeroB
if numeroC > numeroA and numeroC > numeroB:
    maior = numeroC
print('O {}menor{} valor digitado foi {}{}{}.'.format('\033[33m', '\033[m', '\033[4;33m', menor, '\033[m'))
print('O {}maior{} valor digitado foi {}{}{}.'.format('\033[35m', '\033[m', '\033[4;35m', maior, '\033[m'))
