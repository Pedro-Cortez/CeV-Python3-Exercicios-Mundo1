#Conversor de Medidas
distancia = float(input('Informe a distância em metros: '))

#Cálculo de conversão
cm = distancia * 100
mm = distancia * 1000

#Respostas
print('Conversor de medida: \n''\033[1;31m''cm = {}''\033[m''\033[1;33m''\nmm = {}'.format(cm, mm))
