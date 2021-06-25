'''EXERCÍCIO 75
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
cont9 = 0
lista = int(input('Digite um número: ')), int(input('Mais um: ')), int(input('Mais um: ')),int(input('Mais um: '))
pares = lista[0] % 2, lista[1] % 2, lista[2] % 2, lista[3] % 2
print(f'Você digitou os números {lista}')
print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista: # Sem esse if o programa da problema se não tiver o número 3.
    print(f'O valor 3 aparece na {lista.index(3) + 1}ª posição.')
else:
    print('O valor 3 não aparece.')
print('Os valores pares digitados foram', end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end = ' ')







