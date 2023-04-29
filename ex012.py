#Produto com desconto
preco = float(input('\033[33mInforme o valor da mercadoria: R$ \033[m'))

#Cálculo do desconto
desc = preco - preco * (5 / 100)

#Resposta
print('\033[34mO produto com desconto de 5% custa R$ {:.2f}.\033[m'.format(desc))