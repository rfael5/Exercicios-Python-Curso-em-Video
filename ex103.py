'''EXERCÍCIO 103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''

'''MINHA VERSÃO'''

def ficha(nome="desconhecido",gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols != int:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


a = str(input('Nome do jogador: '))
b = input('Número de gols: ')

print(ficha(a,b))


'''VERSÃO DO PROFESSOR

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
"""O código acima está dizendo que se o g for um número o programa funciona normal. Caso contrário, 
caso g não seja um número inteiro, g será igual a 0."""
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
"""O código acima está dizendo que se o usuário não digitar nada em n, a resposta será o parâmetro
opcional que você colocou na função. n.strip quer dizer n sem espaços, lembrando que o comando strip
é aquele comando que tira os espaços."""
'''