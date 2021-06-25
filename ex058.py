'''EXERCÍCIO 58
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''

from random import randint
'''MINHA VERSÃO'''
jogador = ''
computador = randint(1,11) #randint faz escolher um número inteiro randomicamente.
erros = 0
print('Vou pensar em um número. Tente adivinhar.')
while jogador != computador:
    jogador = int(input('Qual número eu pensei? '))
    if jogador != computador:
        erros+= 1
        if computador > jogador:
            print('Mais... Tente outra vez.')
        if computador < jogador:
            print('Menos... Tente outra vez.')

print('~'*35)
print('VOCÊ VENCEU.')
print('Acertou com {} partida(s). Parabéns'.format(erros))


'''VERSÃO PROFESSOR
computador = randint(0,10)
print('Pensei em um número. Tente adivinhar qual.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual número eu pensei? '))
    palpites+= 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns'.format(palpites))'''




