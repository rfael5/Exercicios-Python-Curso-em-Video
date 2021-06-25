'''EXERCÍCIO 20
O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos
alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
p1 = input('Primeiro nome: ')
p2 = input('Segundo nome: ')
p3 = input('Terceiro nome: ')
p4 = input('Quarto nome: ')

lista = [p1,p2,p3,p4]
shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)

