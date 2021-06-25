'''EXERCÍCIO 99
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def maior(*n):
    print('Analisando os valores passados...')
    sleep(0.2)
    for valor in n:
        print(valor,end=' ')
        sleep(0.2)
    print(f'Foram informados {len(n)} valores ao todo.')
    if len(n) > 0:
        print(f'O maior valor informado foi {max(n)}.')
    else:
        print('Não foi informado nenhum valor.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
