#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
print('CALCULO DE VELOCIDADE DE DOWNLOAD')
print()
print()
tam = float(input('Qual o tamanho do arquivo em MB?'))
print()
vel = float(input('Qual a velocidade da internet em Mbps?'))
print()
vels = (tam / vel) / 8
print('O tempo necessário em minutos é', (vels /60))

