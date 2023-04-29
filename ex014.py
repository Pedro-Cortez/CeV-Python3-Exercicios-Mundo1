# Conversor de temperatura ºC → ºF
temp = float(input('\033[32mInforme a temperartura auferida em ºC: \033[m'))

# Cálculo de conversão
fah = (temp * 1.8) + 32

#Resposta
print('\033[1;31mA temperatura de {}ºC corresponde a {:.1f}ºF.\033[m'.format(temp, fah))
