'''EXERCÍCIO 71
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

'''VERSÃO FUNCIONANDO. COM NOTAS DE 100, 5 E 2.'''
n = int(input('Digite um valor: R$'))
cont100 = cont50 = cont20 = cont10 = cont5 = cont2 = cont1 = 0

while n >= 100:
    n -= 100
    cont100 += 1
    if n < 100 and n >= 50:
        while n >= 50:
            n -= 50
            cont50 += 1
    if n < 50 and n >= 20:
        while n >= 20:
            n -= 20
            cont20 += 1
    if n < 20 and n >= 10:
        while n >= 10:
            n -= 10
            cont10 += 1
    if n < 10 and n >= 5:
        while n >= 5:
            n -= 5
            cont5 += 1
    if n < 5 and n >= 2:
        while n >= 2:
            n -= 2
            cont2 += 1
    if n == 1:
        while n == 1:
            n -= 1
            cont1 += 1

print(f'Sobra: {n}')
if cont100 > 0:
    print(f'Serão sacadas {cont100} cédulas de R$100.00.')
if cont50 > 0:
    print(f'Serão sacadas {cont50} cédulas de R$50.00.')
if cont20 > 0:
    print(f'Serão sacadas {cont20} cédulas de R$20.00.')
if cont10 > 0:
    print(f'Serão sacadas {cont10} cédulas de R$10.00.')
if cont5 > 0:
    print(f'Serão sacadas {cont5} cédulas de R$5.00.')
if cont2 > 0:
    print(f'Serão sacadas {cont2} cédulas de R$2.00.')
if cont1 > 0:
    print(f'Serão sacadas {cont1} cédulas de R$1.00')


'''1ª TENTATIVA. DEU ERRADO.
n = 272
cn = n
vn = n
dn = n
un = n
rn = 0
if cn % 50 != 0:
    while cn % 50 != 0:
        cn = cn - 1
        rn = n - cn
        if rn >= 20 and rn < 50:
            vn = rn
            while vn % 20 != 0:
                vn = vn - 1
                dn = rn - vn
        elif rn >= 10 and rn < 20:
            dn = rn
            while dn % 10 != 0:
                dn = dn - 1
                un = rn - dn





print(f'Você quer sacar {cn / 50} cédulas de R$50.00')
print(f'Você quer sacar {vn / 20} cédulas de R$20.00')
print(f'Você quer sacar {dn / 10} cédulas de R$10.00')
print(f'Você quer sacar {un} cédulas de R$1.00')'''

'''VERSÃO DO PROFESSOR
valor = int(input('Que valor você quer sacar?: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Serão impressas {totced} notas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break'''


