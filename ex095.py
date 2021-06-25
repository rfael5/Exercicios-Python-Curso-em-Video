'''EXERCÍCIO 95
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
de detalhes do aproveitamento de cada jogador.'''

'''MINHA VERSÃO - Consegui fazer o programa, mas não consegui formatar pra ele aparecer bonito.
jogador = dict()
dados = list()
while True:
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
    dados.append(jogador.copy())
    cont = str(input('Quer continuar?[S/N]:')).upper()
    while cont not in 'SN':
        cont = str(input('Quer continuar?[S/N]:')).upper()
    if cont == 'N':
        break
print('-='*30)
print(jogador)
print(dados)
for d in enumerate(dados):
    print(d)
print('-='*30)
while True:
    lev = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if lev <= len(dados):
        print(f'Mostrando dados do jogador {dados[lev]["Jogador"]}.')
        for e,g in enumerate(dados[lev]['Gols']):
            print(f'No jogo {e} ele marcou {g} gols.')
        print('=-'*30)
    if lev > len(dados) and lev != 999:
        print(f'Este número não está na lista. (Tamanho da lista = {len(dados)})')
        print('=-'*30)
    if lev == 999:
        break
print('<<<ENCERRADO>>>')'''

'''VERSÃO DO PROFESSOR'''
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
               #^ Isso é pra colocar espaço entre os dados
print()
print('-'*40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com códico {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<<VOLTE SEMPRE>>')


