'''EXERCÍCIO 50
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1

if cont == 1:
    print('Você informou 1 número par e seu valor é {}'.format(soma))
else:
    print('Você informou {} números pares, e a soma deles é {}.'.format(cont,soma))