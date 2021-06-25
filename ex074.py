'''EXERCÍCIO 74
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
lista = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)

print(f'Os números sorteados foram: {lista}')
print(f'O menor deles é: {min(lista)}')
print(f'O maior deles é: {max(lista)}')