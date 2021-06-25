'''EXERCÍCIO 106
Make a mini-system that utilizes Python Interactive Help. The user is going to type the command and the
manual will show up. When the user types the word 'FIM' ('END'), the program will close.
Important: Use colors.'''

'''MINHA VERSÃO (NÃO USEI FUNÇÃO)

while True:
    print('\033[0;30;42m~'*30)
    print('\033[0;30;42mSISTEMA DE AJUDA pyHELP')
    print('\033[0;30;42m~'*30)
    ajuda = str(input('\033[mBiblioteca ou função: '))
    if ajuda == 'fim':
        break
    else:
        print('\033[0;30;44m~'*30)
        print(f'Acessando o manual do comando {ajuda}.')
        print('~'*30)
        print(f'\033[7;0;40m')
        help(ajuda)
'''

'''VERSÃO DO PROFESSOR'''
from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~'*tam)
    print(f'{  msg}')
    print('~' * tam)
    print(c[0],end='')
    sleep(1)

#Programa Principal
while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    comando = (str(input('Função ou Biblioteca: ')))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO',1)