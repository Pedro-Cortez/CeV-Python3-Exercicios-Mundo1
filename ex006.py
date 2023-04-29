#Cálculo do dobro, triplo e raiz quadrada
numero = float(input('Informe um número qualquer: '))

cores = {'limpa': '\033[m', 'azul': '\033[1;34m', 'lilas': '\033[1;35m', 'verde': '\033[1;32m'}

#Resposta
print('O dobro é {}{}{}, o triplo é {}{}{} e a raiz quadrada é {}{:.2f}{}.'
      .format(cores['azul'], (numero * 2), cores['limpa'], cores['lilas'], (numero * 3), cores['limpa'], cores['verde'], (numero ** (1/2)), cores['limpa']))
