#Verificar primeiras letras de uma cadeia de strings
cidade = str(input('\033[31mInforme a cidade onde nasceu: \033[m')).strip()

#Análise do nome
div = cidade.split()
cid = div[0].title()


#Resposta
print('\033[36m',cid =='Santo')

#Gabarito
print(cidade[:5].upper() == 'SANTO','\033[m')