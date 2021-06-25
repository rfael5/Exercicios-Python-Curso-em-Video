'''EXERCÍCIO 59
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
opção = 0
while opção != 5:
    opção = int(input('O que fazer com os dois valores? '))
    if opção == 1:
        print('A soma de {} e {} é {}.'.format(v1,v2,v1 + v2))
    elif opção == 2:
        print('{} multiplicado por {} é {}.'.format(v1,v2,v1 * v2))
    elif opção == 3:
        if v1 > v2:
            print('Dos dois valores, o maior é {}.'.format(v1))
        elif v1 == v2:
            print('Os dois valores são iguais.')
        else:
            print('Dos dois valores, o maior é {}.'.format(v2))
    elif opção == 4:
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))

print('FIM')