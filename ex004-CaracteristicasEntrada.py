#Entrada do usuário
algo = input('Digite aqui: ')
#Características do valor de entrada
print('O tipo primitivo desse valor é ', '\033[1;32m', type(algo), '\033[m')
print('Só tem espaços?', '\033[1;31m', algo.isspace(), '\033[m')
print('É um número?', '\033[1;32m', algo.isnumeric(), '\033[m')
print('É um valor alfanumérico?', '\033[1;33m', algo.isalnum(), '\033[m')
print('É um valor alfabético?', '\033[1;34m', algo.isalpha(), '\033[m')
print('O valor possui apenas maiúsculas?', '\033[1;35m', algo.isupper(), '\033[m')
print('O valor possui apenas minúsculas?', '\033[1;36m', algo.islower(), '\033[m')
print('O valor está capitalizado?', '\033[7;30;41m', algo.istitle(), '\033[m')
