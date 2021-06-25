'''EXERCÍCIO 38
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma
mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior. Os dois valores são iguais.'''

v1 = int(input('Primeiro número: '))
v2 = int(input('Segundo número '))

if v1 > v2:
    print('O PRIMEIRO valor é o maior.')
elif v2 > v1:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior. Os dois valores são iguais.')