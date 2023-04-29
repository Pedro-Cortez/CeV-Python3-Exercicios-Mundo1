#Buscador do sobrenome "Silva"
nome = str(input('\033[31mQual seu nome completo?\n')).strip()

#Funcionamento do buscador
nome_final = nome.title()

#Resultado
print('O nome do usuário possui Silva?\033[m \033[33m{}\033[m'.format('Silva' in nome_final))
