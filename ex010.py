#Conversor de real para dólar
grana = float(input('Digite o valor disponível na carteira: R$ '))

#Cálculo da convesão
dolar = grana / 3.27

#Resposta
print('Você poderá comprar US$ \033[4;30;42m{:.2f}\033[m.'.format(dolar))
