'''EXERCÍCIO 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
OBRIGATÓRIO nas eleições.'''

'''MINHA SOLUÇÃO
def voto(age):
    r = 2018 - age

    if r >= 18:
        print(f'Com {r} anos: Seu voto é OBRIGATÓRIO')
    elif r >=16 and r < 18:
        print(f'Com {r} anos: Seu voto é OPCIONAL.')
    elif r >= 65:
        print(f'Com {r} anos: Seu voto é OPCIONAL')
    elif r < 16:
        print(f'Com {r} anos: Você não pode votar.')



resp = int(input('Qual ano você nasceu? '))
voto(resp)
'''

'''SOLUÇÃO DO PROFESSOR'''
def voto(ano):
    from datetime import date
    #Quando você importa bibliotecas dentro da função, você economiza memória.
    atual = date.today().year
    idade = atual - ano
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

resp = int(input('Em qual ano você nasceu?: '))
print(voto(resp))

