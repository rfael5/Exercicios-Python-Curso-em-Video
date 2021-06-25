'''EXERCÍCIO 90
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

notas = {'aluno': str(input('Nome:')),'nota': int(input('Nota: '))}

print('-=' * 30)
print(f'O nome do aluno é {notas["aluno"]}')
print(f'Sua média é {notas["nota"]}')
if notas["nota"] < 5:
    print('Situação: Reprovado')
else:
    print('Situação: Aprovado')