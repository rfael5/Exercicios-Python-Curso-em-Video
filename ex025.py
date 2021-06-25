'''EXERCÍCIO 25
Crie um programa que leia o nome de uma pessoa e verifique se ela tem 'Silva' no nome.'''

nome = str(input('Qual é seu o nome completo? ')).upper().strip().split()

print('Seu nome tem "Silva"? {}'.format('SILVA' in nome))