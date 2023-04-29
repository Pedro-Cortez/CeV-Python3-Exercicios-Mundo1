# Antecessor e Sucessor
numero = int(input('Digite um número: '))

cores = {'limpa': '\033[m', 'vermelho': '\033[1;31m', 'lilas': '\033[1;35m', 'azul': '\033[1;36m'}
# Resposta
print('O antecessor de {}{}{} é {}{}{} e o sucessor é {}{}{}.'
      .format(cores['azul'], numero, cores['limpa'], cores['lilas'],
              (numero - 1), cores['limpa'], cores['vermelho'], (numero + 1), cores['limpa']))
