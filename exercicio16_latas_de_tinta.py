#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print('CALCULO DE LATAS NECESSÁRIAS')
print()
print()
nome = input('Antes de começar, qual é o seu nome? ')
print()
print()
metros = float(input(f'Informe o tamanho da área a ser pintada em metros quadrados {nome}: '))
print()
tinta = print('A quantidade de latas de tintas necessárias:',(metros / 54))

