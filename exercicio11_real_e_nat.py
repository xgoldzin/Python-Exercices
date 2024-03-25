# Exercicio 11: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
print('OPERAÇÕES COM NÚMEROS INTEIROS E NÚMERO REAL')
print()
print()
nome = input('Antes de começarmos, qual é o seu nome?')
print()
n1 = int(input(f'Informe o primeiro numero inteiro {nome}: '))
print()
n2 = int(input(f'Informe o segundo número inteiro {nome}: '))
print()
n3 = float(input(f'Informe um úmero real {nome}: '))
print()
print()
print('O produto do dobro do primeiro com metade do segundo número:', (n1 *2) + (n2 / 2))
print()
print('A soma do triplo do primeiro com o terceiro:', (n1 * 3) +(n3))
print()
print('O terceiro número elevado ao cubo:',(n3 ** 3))
