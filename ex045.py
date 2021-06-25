'''EXERCÍCIO 45
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
#_____________COMO GUANABARA FEZ________________
print('''ESCOLHA
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
jogador = int(input('Qual sua escolha? '))

g = 'VOCÊ GANHOU!' # Esse foi ideia minha.
p = 'VOCÊ PERDEU.'
e = 'EMPATE.'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('='*20)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
#Colocou itens + jogador ou pc entre colchetes. Assim os números de 0 a 2 vão corresponder a posição dos itens na lista 'itens'.
print('='*20)
if pc == 0:
    if jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU.')
    elif jogador == 0:
        print('EMPATE')
    else:
        print('COMANDO INVALIDO')

elif pc == 1:
    if jogador == 0:
        print(p)
    elif jogador == 2:
        print(g)
    elif jogador == 1:
        print(e)
    else:
        print('COMANDO INVALIDO')

elif pc == 2:
    if jogador == 0:
        print(g)
    elif jogador == 1:
        print(p)
    elif jogador == 2:
        print(e)
    else:
        print('COMANDO INVALIDO')

'''
_________COMO EU FIZ______________________

a = 'JOGADOR - PEDRA'
b = 'JOGADOR - PAPEL'
c = 'JOGADOR - TESOURA'
g = 'VOCÊ GANHOU!'
p = 'VOCÊ PERDEU.'
e = 'EMPATE.'
if pc == 0:
    print('PC - PEDRA')
    if jogador == 1:
        print(b)
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print(c)
        print('VOCÊ PERDEU.')
    elif jogador == 0:
        print(a)
        print('EMPATE')
    else:
        print('COMANDO INVALIDO')

elif pc == 1:
    print('PC - PAPEL')
    if jogador == 0:
        print(a)
        print(p)
    elif jogador == 2:
        print(c)
        print(g)
    elif jogador == 1:
        print(b)
        print(e)
    else:
        print('COMANDO INVALIDO')

elif pc == 2:
    print('PC - TESOURA')
    if jogador == 0:
        print(a)
        print(g)
    elif jogador == 1:
        print(b)
        print(p)
    elif jogador == 2:
        print(c)
        print(e)
    else:
        print('COMANDO INVALIDO')'''