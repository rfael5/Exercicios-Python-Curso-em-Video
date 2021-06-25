'''EXERCÍCIO 66
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

cont = tot = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        print('Acabou.')
        break
    cont += 1
    tot = tot + n
    '''Antes eu tinha colocado o cont e o tot dentro de um else. Mas na aula mostrou que
    não precisa. É só mudar a indetação.'''
print(f'Você digitou {cont} valores e a soma deles é {tot}.')


