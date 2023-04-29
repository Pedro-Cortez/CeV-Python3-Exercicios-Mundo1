#Cálculo de aumento em função do valor de salário-base
Sal_Base = float(input('Informe o salário atual do colobarador: R$'))

#Cálculo
if Sal_Base <= 1250.00:
    maior_aumento = (Sal_Base * 15 / 100) + Sal_Base
    print('O novo salário para quem recebe \033[4;32mR${:.2f}\033[m será de \033[4;34mR${:.2f}\033[m.'.format(Sal_Base, maior_aumento))
if Sal_Base > 1250.00:
    menor_aumento = (Sal_Base * 10 / 100) + Sal_Base
    print('O novo salário para quem recebe \033[4;32mR${:.2f}\033[m será de \033[4;34mR${:.2f}\033[m'.format(Sal_Base, menor_aumento))

#Gabarito
if Sal_Base <= 1250.00:
    novo = Sal_Base + (Sal_Base * 15 / 100)
else:
    novo = Sal_Base + (Sal_Base * 10 / 100)
print('\033[31mO novo salário para quem ganha R${:.2f} será de R${:.2f}.\033[m'.format(Sal_Base, novo))
