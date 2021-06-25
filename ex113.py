'''EXERCÍCIO 113
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de
um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

'''MINHA VERSÃO'''
def leiaInt(msg):
    ok = False
    while True:
        try:
            a = int(input(msg))
        except ValueError:
            print('\033[0;31mERRO: Por favor digite um número inteiro válido.\033[m')
        else:
            ok = True
            return a
        if ok:
            break

def leiaFloat(msg):
    ok = False
    while True:
        try:
            b = float(input(msg))
        except ValueError:
            print('\033[0;31mERRO: Por favor digite um número real válido.\033[m')
        else:
            ok = True
            return b

m = leiaInt('Digite um inteiro: ')
n = leiaFloat('Digite um real: ')

print(f'O valor inteiro digitado foi {m} e o real foi {n}.')


'''VERSÃO DO PROFESSOR
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor digite um número inteiro válido.\033[m')
            continue
            # ^ Esse continue faz o programa voltar para o início do looping.
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num

num1 = leiaInt('Digite um Inteiro: ')
num2 = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {num1} e o real foi {num2}.')'''




