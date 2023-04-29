#Cálculo do valor de passagem rodoviária
viagem = float(input('Informe a distância do trecho (km): '))

#Cálculo
if viagem <= 200:
    preco = viagem * 0.5
else:
    preco = viagem *0.45

#Resposta
print('{}A passagem custa {}R${:.2f}.{}'.format('\033[1;35m', '\033[4m', preco, '\033[m'))
