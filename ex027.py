'''EXERCÍCIO 27
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).capitalize().strip().split()

print('Muito prazer em te conhecer {}!'.format(nome[0].capitalize()))
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1].capitalize()))

'''
OUTRA FORMA - com reverse
print('Muito prazer em te conhecer {}!'.format(nome[0].capitalize()))
print('Seu primeiro nome é {}.'.format(nome[0]))
nome.reverse()
print('Seu último nome é {}.'.format(nome[0].capitalize()))
'''