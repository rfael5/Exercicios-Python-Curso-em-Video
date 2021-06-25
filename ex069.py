'''EXERCÍCIO 69
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
cont18 = 0
conth = 0
contm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    continuar = str(input('Quer continuar?: '))
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm20 += 1
    if continuar == 'n':
        break

print(f'Pessoas com mais de 18 anos: {cont18}')
print(f'Pessoas do sexo masculino: {conth}')
print(f'Mulheres com mais de vinte anos: {contm20}')
