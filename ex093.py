'''EXERCÍCIO 93
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o
campeonato.'''

jogador = dict()
jogador['Jogador'] = str(input('Nome do Jogador: '))
partidas = int(input('Partidas jogadas:'))
jogador['Partidas'] = partidas
gols = list()
for v in range(0,partidas):
    g = int(input(f'Quantos gols na partida {v}:'))
    gols.append(g)
total = sum(gols)
jogador['Gols'] = gols
jogador['Total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f"O jogador {jogador['Jogador']} jogou {jogador['Partidas']} partidas.")
for n,c in enumerate(jogador['Gols']):
    print(f'->Na partida {n} ele marcou {c} gols.')
print(f"Foi um total de {jogador['Total']} gols.")
