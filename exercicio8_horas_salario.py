# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.#
print('CALCULO DE SALÁRIO MENSAL')
print()
print()
nome = input('Antes de começarmos qual é o seu nome? ')
print()
ganho = float(input(f'Quanto você ganha por hora {nome}?(Caso seja numero quebrado informe com um ponto final) '))
print()
horas = float(input(f'Quantas horas você trabalhou esse mês {nome}? '))
print('O salário total desse mês é: ', (ganho * horas))
print()
print('Agradecemos a preferência!')