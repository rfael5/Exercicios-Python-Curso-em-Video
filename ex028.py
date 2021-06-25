'''EXERCÍCIO 28
Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
computador = randint(0,5) #randint faz escolher um número inteiro randomicamente.
print('Vou pensar em um número. Tente adivinhar.')
jogador = int(input('Qual número eu pensei?'))
if jogador == computador:
    print('Você venceu! Muito bom.')
else:
    print('Eu venci.')

