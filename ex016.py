'''EXERCÍCIO 16
Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção inteira.'''

from math import trunc
num = float(input('Digite um número: '))
int = trunc(num)

print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int))