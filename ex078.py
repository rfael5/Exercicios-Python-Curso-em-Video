'''EXERCÍCIO 78
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista. '''

'''MINHA VERSÃO
lista = [int(input('Valor da posição 0: ')),int(input('Valor da posição 1: ')),
         int(input('Valor da posição 2: ')),int(input('Valor da posição 3: ')),
         int(input('Valor da posição 4: '))]

print(f'Você digitou os valores {lista}.')
print(f'O menor valor da lista é {min(lista)} e está na posição ',end='')
for p,v in enumerate(lista):
    if min(lista) == v:
        print(f'{p }',end=' ')
print()
print(f'O maior valor da lista é {max(lista)} e está na posição ',end='')
for p,v in enumerate(lista):
    if max(lista) == v:
        print(f'{p }',end=' ')
print()
'''

'''VERSÃO DO PROFESSOR'''
lista = []
for c in range(0,5):
#o comando 'append' adiciona valores à lista.
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {lista}.')
print(f'O maior valor da lista é {max(lista)} e sua posição é ',end='')
'''Em enumerate, a primeira letra (nesse caso p) representa a posição do valor na lista, e a segunda
letra (no caso c) representa o valor.'''
for p,c in enumerate(lista):
    if max(lista) == c:
        print(p, end=' ')
print()
print(f'O menor valor da lista é {min(lista)} e sua posição é ',end='')
for p,c in enumerate(lista):
    if min(lista) == c:
        print(p,end=' ')
print()



