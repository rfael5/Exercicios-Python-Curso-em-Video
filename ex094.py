'''EXERCÍCIO 94
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em
um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = list()
idades = list()
mulheres = list()
maiormedia = list()
pessoas = dict()
while True:
    nome = str(input('Nome: '))
    pessoas['nome'] = nome
    sexo = str(input('Sexo[M/F]: ')).upper()
    while sexo != 'M' and sexo != 'F':
        print('ERRO! Por favor, digite M ou F.')
        sexo = str(input('Sexo[M/F]: ')).upper()
    if sexo == 'F' or sexo == 'M':
        pessoas['sexo'] = sexo
    idade = int(input('Idade: '))
    idades.append(idade)
    pessoas['idade'] = idade
    dados.append(pessoas.copy())
    if sexo == 'F':
        mulheres.append(nome)
    cont = str(input('Quer continuar?[S/N]: ')).upper()
    while cont != 'S' and cont != 'N':
        print('ERRO! Responda apenas S ou N.')
        cont = str(input('Quer continuar?[S/N]: ')).upper()
    if cont == 'N':
        break
mediaidade = sum(idades)/len(dados)
print('-='*30)
print(pessoas)
print(dados)
print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'A média de idade é de {mediaidade} anos.')
print(f'As mulheres cadastradas foram {mulheres}')
for e in dados:
    if e['idade'] > mediaidade:
        print(f'nome = {e["nome"]};sexo = {e["sexo"]};idade = {e["idade"]}')
print('<<ENCERRADO>>')
