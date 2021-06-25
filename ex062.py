'''EXERCÍCIO 62
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
max = 0
mais = 10

while mais != 0:
    max = max + mais
    while cont <= max:
        print('{}-'.format(termo),end='')
        termo += razão
        cont += 1
    mais = int(input('Quantos a mais?: '))
print('FIM')
print('{} termos'.format(cont - 1))








