'''EXERCÍCIO 51
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

termo1 = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = termo1 + (10-1) * razao #fórmula para calcular décimo termo.

for c in range(termo1,decimo+razao,razao):
    print(c,end=' - ')
print('Acabou')