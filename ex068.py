'''EXERCÍCIO 68
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.'''

from random import randint
'''MINHA VERSÃO'''
contv = 0
while True:
    num = int(input('Digite um número: '))
    op = str(input('Par ou Impar?[P/I]: ')).upper()
    pc = randint(0, 9)
    tot = pc + num
    resp = ''
    if tot % 2 == 0 and op == 'P':
        print(f'Você escolheu {num} e o pc {pc}. A soma é {tot}.')
        print('PAR.')
        print('Você venceu.')
    elif tot % 2 != 0 and op == 'I':
        print(f'Você escolheu {num} e o pc {pc}. A soma é {tot}.')
        print('IMPAR.')
        print('Você venceu')
    else:
        if op != 'P' and op != 'I':
            print('Opção invalida. Você tem que digitar p ou i.')
        print(pc)
        print('Você perdeu.')
        break
    contv += 1

if contv == 1:
    print(f'Você venceu {contv} vez.')
elif contv == 0:
    print('Você não venceu nenhuma vez.')
else:
    print(f'Você venceu {contv} vezes.')

'''VERSÃO DO PROFESSOR
contv = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0] 
        '''Essa é a saida que ele usou pro caso do usuário digitar algo diferente de P ou I.'''
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            contv += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            contv += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {contv} vezes.')'''
