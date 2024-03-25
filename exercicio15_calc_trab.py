#exercicio15:Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
print('CALCULO DE SALÁRIO LÍQUIDO')
print()
print()
nome = input('Antes de começarmos, informe seu nome: ')
print()
print()
salr = float(input(f'Qual seu salário bruto {nome}?'))
print()
salariob = print('+Salário Bruto ; R$', salr)
imposto1 = (salr * 11) /100
imposto2 = (salr * 8) /100
imposto3 = (salr *5) /100
print('- IR (11%) : R$', imposto1)
print('- INSS (8%) : R$', imposto2)
print('- Sindicato (5%) : R$', imposto3)
impostos = (imposto1 + imposto2 + imposto3)
salarioL = print('=Salário líquido : R$',(salr - impostos))
