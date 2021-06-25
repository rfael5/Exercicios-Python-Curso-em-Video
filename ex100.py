'''EXERCÍCIO 100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.'''

'''MINHA VERSÃO'''

'''
from random import randint
from time import sleep
números = []
def sorteia(a):
    for n in range(0,5):
        a = randint(0,10)
        números.append(a)
    print('Sorteando os 5 valores da lista:',end = ' ')
    sleep(0.2)
    for valores in números:
        print(valores,end = ' ')
        sleep(0.3)
    print('PRONTO!')
def somaPar(b):
    b = list()
    for valores in números:
        if valores % 2 == 0:
            b.append(valores)
    print(f'Somando os valores pares de {números}, temos {sum(b)}.')

sorteia(números)
somaPar(números)
'''

'''VERSÃO DO PROFESSOR'''

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    sleep(0.3)
    for valores in range(0,5):
        a = randint(0,10)
        lista.append(a)
        print(a,end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valores in lista:
        if valores % 2 == 0:
            soma += valores
    print(f'Somando os valores de {lista}, temos {soma}.')

números = list()
sorteia(números)
somaPar(números)

