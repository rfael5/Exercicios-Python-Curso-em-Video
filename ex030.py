'''EXERCÍCIO 30
Crie um programa que leia um número inteiro e diga se ele é par ou impar.'''

número = int(input('Digite um número: '))
if número % 2 == 0:
    print('O número {} é PAR.'.format(número))
else:
    print('O número {} é IMPAR.'.format(número))