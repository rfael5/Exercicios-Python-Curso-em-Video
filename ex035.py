'''EXERCÍCIO 35
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem
ou não formar um triângulo.'''

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))


if l1 > (l2-l3) and l1 < (l2+l3) and l2 > (l1 - l3) and l2 < (l1 + l3) and l3 > (l1 - l2) and l3 < (l1 + l2)
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')