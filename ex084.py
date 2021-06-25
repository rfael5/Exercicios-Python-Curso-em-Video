'''EXERCÍCIO 84
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dados = []
peso = []
pesop = []
pesol = []

while True:
    nome = [str(input('Nome: ')), float(input('Peso: '))]
    dados.append(nome)
    peso.append(nome[1])
    c = str(input('Quer continuar? '))
    if c == 'n':
        break

for p in dados:
    if p[1] == max(peso):
        pesop.append(p[0])
    elif p[1] == min(peso):
        pesol.append(p[0])

print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'As pessoas mais leves são {pesol}, pesando {min(peso)}kg.')
print(f'As pessoas mais pesadas são {pesop}, pesando {max(peso)}kg.')




