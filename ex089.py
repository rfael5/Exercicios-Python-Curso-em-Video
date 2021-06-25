'''EXERCÍCIO 89
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''
'''
lista = []
dados = []
listamedia = []
media = []

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2:')))
    dados.append(lista[:])
    listamedia.append(lista[0])
    listamedia.append((lista[1]+lista[2]) / 2)
    media.append(listamedia[:])
    cont = str(input('Quer continuar?: '))
    lista.clear()
    listamedia.clear()
    if cont in 'Nn':
        break

for n,v in enumerate(media):
    print(n,v)

while True:
    notas = int(input('Mostrar as notas de qual aluno?'))
    if notas != 999:
        print(dados[notas])
    else:
        break'''

'''VERSÃO DO PROFESSOR'''

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    cont = str(input('Quer continuar? [S/N]: '))
    if cont in 'Nn':
        break

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for n, a in enumerate(ficha):
    print(f'{n:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    aluno = int(input('Mostrar notas de qual aluno?[999 interrompe]: '))
    if aluno == 999:
        break
    if aluno <= len(ficha) - 1:
        print(f'As notas de {ficha[aluno][0]} são {ficha[aluno][1]}.')
print('<<< VOLTE SEMPRE >>>')
