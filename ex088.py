'''EXERCÍCIO 88
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
lista composta.'''
'''MINHA SOLUÇÃO'''
from random import choice
lista = list(range(1,61))
sorteados = []
jogos = 0

a = int(input('Quantos jogos você quer fazer?: '))
for v in range(0,a):
    while len(sorteados) < 6:
        numero = choice(lista)
        if numero not in sorteados:
            sorteados.append(numero)
    print(sorted(sorteados))
    sorteados.clear()

'''SOLUÇÃO DO PROFESSOR
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA    ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])#Fez uma cópia da lista e colocou na lista 'jogos'
    lista.clear()
    tot +=1
print('-=' * 3,f' SORTEANDO {quant} JOGOS','-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 3, '<BOA SORTE! >','-=' * 3)'''

