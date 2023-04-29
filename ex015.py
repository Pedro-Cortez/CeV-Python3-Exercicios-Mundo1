#Aluguel de Carros
km = int(input('\033[1;35mInforme a quantidade de quilômetros percorridos: '))
dias = float(input('Quantidade de dias do contrato de aluguel: \033[m'))

#Cálculo do valor do aluguel
aluguel = (km * 0.15) + (dias * 60)

#Resultado
print('\033[31mO valor total do contrato de aluguel é de R$ {:.2f}\033[m'.format(aluguel))