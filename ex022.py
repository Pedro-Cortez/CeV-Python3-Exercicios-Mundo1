#Analisador de textos
nome = str(input('Digite seu nome completo: ')).strip()
#Análise de cadeia de strings
separa = nome.split()
junta = ''.join(separa)
#Imprimir respostas
print('\033[33m~=' * 15)
print('\tAnalise de Nome Próprio')
print('~=' * 15)
print('\033[mEm letras maiúsculas: \033[33m{}\033[m.'.format(nome.upper()))
print('Em letras minúsculas: \033[33m{}\033[m.'.format(nome.lower()))
print('Contagem de letras do nome completo: \033[33m{}\033[m letras.'.format(len(junta)))
print('Contagem de letra primeiro nome: \033[33m{}\033[m letras.'.format(len(separa[0])))

print('\nContagem alternativa de letras do nome comepleto: \033[31m{}\033[m.'.format(len(nome) - nome.count(' ')))
print('Contagem alternativa de letras do primeiro nome: \033[31m{}\033[m.'.format(nome.find(' ')))