'''EXERCÍCIO 91
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou
o maior número no dado.'''

'''SOLUÇÃO DO PROFESSOR'''
from random import randint
from operator import itemgetter

resultados = {'Jogador 1':randint(1,6),
              'Jogador 2':randint(1,6),
              'Jogador 3':randint(1,6),
              'Jogador 4':randint(1,6)}
em_ordem = list()
for k, v in resultados.items():
    print(f' O {k} tirou {v}')

print('-=' * 30)
print('RESULTADOS')

em_ordem = sorted(resultados.items(), key=itemgetter(1), reverse=True)
'''Pra função sorted funcionar com dicionários você precisa importar a função "itemgetter".
Não sei pq isso.'''

'''Se você colocar "itemgetter(0)", ele vai usar como base a key do dicionário, se você colocar
"itemgetter(1)", ele vai usar como base o valor no dicionário.'''

for r,v in enumerate(em_ordem):
    print(f'{r+1}º Lugar: {v[0]} tirou {v[1]}.')






