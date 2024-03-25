#Exercicio13:Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
print('*'*25)
print('* CALCULO DE PESO IDEAL *')
print('*'*25)
print()
print()
nome= input('Antes de começar, qual o seu nome?')
print()
h = float(input(f'Qual a sua altura(escreva com ponto final) {nome}? '))
print()
print('O seu peso ideal em kilos caso seja homem é:', (72.7*h) - 58)
print()
print('O seu peso ideal em kilos caso seja mulher é:', (62.1*h) - 44.7)
