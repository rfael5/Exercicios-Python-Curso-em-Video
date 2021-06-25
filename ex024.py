'''EXERCÍCIO 24
Crie um programa que leia o nome de uma cidade e diga se ela tem ou não o nome 'Santo'.'''

cidade = str(input('Em qual cidade você nasceu? ')).upper().strip().split()

print(cidade[0] == 'SANTO')