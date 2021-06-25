'''EXERCÍCIO 54
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
menor = 0
maior = 0
for c in range(1,8):
    ano = int(input('Em qual ano a {}ª pessoa nasceu? '.format(c)))
    b = date.today().year
    i = b - ano
    if i > 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} das 7 pessoas são maiores de idade.'.format(maior))
print('{} das 7 pessoas são menores de idade.'.format(menor))