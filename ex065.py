'''EXERCÍCIO 65
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

'''MINHA VERSÃO'''
num = int(input('Digite um número: '))
c = str(input('Quer continuar?[S/N]: '))
cont = 1
tot = num
med = 0
maior = num
menor = num
while c == 's':
    num = int(input('Digite um número: '))
    c = str(input('Quer continuar?[S/N]: '))
    cont += 1
    tot = tot + num
    med = tot / cont
    if num == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


print('Você digitou {} números. A soma deles é {} e a média deles é {:.2f}.'.format(cont,tot,med))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))

'''VERSÃO DO PROFESSOR
c = 'S'
med = cont = tot = maior = menor = 0
while c in 'Ss':
    num = int(input('Digite um valor: '))
    cont += 1
    tot = tot + num
    if cont == 1: 
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    c = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]

med = tot / cont #Ele pos a conta da média só no final
print('Você digitou {} valores. A soma deles é {} e a média é {}.'.format(cont, tot, med))
print('O maior deles é {} e o menor é {}.'.format(maior,menor))'''