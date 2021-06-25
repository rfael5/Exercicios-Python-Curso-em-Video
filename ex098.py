'''EXERCÍCIO 98
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e
passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def contador(a,b,c):
    print('-=' * 20)
    if c < 0:
        c = c * (-1)
    if c == 0:
        c = 1
    if a < b:
        print(a,end=' ')
        while a < b:
            a += c
            if a <= b:
                print(a,end=' ')
            sleep(0.3)
        print('FIM!')
    elif a > b:
        print(a,end=' ')
        while a > b:
            a -= c
            if a >= b:
                print(a,end=' ')
            sleep(0.3)
        print('FIM!')


contador(1,10,1)
contador(10,1,2)
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))

