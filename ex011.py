#Quantidade de tinta
largura = float(input('Informe a largura do ambiente (m): '))
altura = float(input('informe a altura do ambiente (m): '))

#Cálculo da área que receberá a tinta
area = largura * altura

#Resposta
print('\033[1;31mO ambiente possui área de {}m².'.format(area))
print('Você precisará de {:.1f}l de tinta para esta área.\033[m'.format(area / 2))
