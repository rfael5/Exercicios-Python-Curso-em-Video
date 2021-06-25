'''EXERCÍCIO 82
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

'''MINHA SOLUÇÃO'''
pares = []
impares = []

while True:
    n = int(input('Digite um valor: '))
    c = str(input('Quer continuar? [s/n] '))
    if c not in 'sn':
        print('Opção invalida.')
        c = str(input('Quer continuar? [s/n] '))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    if c in 'n':
        break
print(f'Os números pares digitados são {pares}.')
print(f'Os números ímpares digitados são {impares}.')
tudo = pares + impares
print(f'A lista completa é {tudo}.')

'''SOLUÇÃO PROFESSOR
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [s/n] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')'''