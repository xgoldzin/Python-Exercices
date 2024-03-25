#Exercicio17:Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math
print('Calculo de tinta necessária')
print()
print()
m = float(input('Informe quantos m² a serem pintados:'))
print()
latas = m /108
lata = math.ceil(latas)
print(f'Serão necessárias {lata} lata(s) e custará R$', (lata * 80.00))
print()
galoes = m / 21.6
galao = math.ceil(galoes)
print(f'Serão necessários {galao} galão(ões) e custará R$', (galao *25,00))
print()
if m >  108 :
    lata = round(m / 108)
    m -= lata * 108
    if m < 108 and m > 0 :
        galoes = math.ceil(m / 21.6)
        m = 0
print(f'Serão necessarias {lata} lata(s) e {galoes} galão(ões)')
