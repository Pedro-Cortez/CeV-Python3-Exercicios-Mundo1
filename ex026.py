#Analisando letras de uma frase
frase = str(input('Digite uma frase: ')).strip()

#Analisando a frase
frase_final = frase.lower()

print('A letra \033[31mA\033[m aparece \033[34m{}\033[m vezes na frase.'.format(frase_final.count('a')))
print('A primeira letra \033[31mA\033[m aparace na posição \033[34m{}\033[m.'.format(frase_final.find('a')+1))
print('A última letra \033[31mA\033[m aparece na posição \033[34m{}\033[m.'.format(frase_final.rfind('a')+1))
