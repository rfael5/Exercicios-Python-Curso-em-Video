'''EXERCÍCIO 92
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em
um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
aposentar.'''
'''MINHA VERSÃO'''
from datetime import datetime
cadastro = {'Nome':str(input('Nome: ')),
            'Idade':datetime.now().year - int(input('Data de Nascimento: ')),
            'Carteira de Trabalho':int(input('Carteira de Trabalho(0 = Não tem): '))}

if cadastro['Carteira de Trabalho'] != 0:
    cadastro.update({'Ano de Contratação':int(input('Ano de Contratação: '))})
    cadastro.update({'Salário':float(input('Salário: '))})
    cadastro.update({'Aposentadoria':cadastro['Idade'] + (cadastro['Ano de Contratação'] + 35)-datetime.now().year})


for k,v in cadastro.items():
    print(f'{k} tem o valor {v}')

'''VERSÃO DO PROFESSOR
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira'] = int(input('Carteira de Trabalho(0 não tem): '))

if dados['carteira'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year

print('-='*30)
for k,v in dados.items():
    print(f'{k} tem o valor {v}.')'''

