'''EXERCÍCIO 39
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua
idade, se ele ainda vai se alistar no serviço militar, se é a hora de se alistar, ou se
já passou o tempo de alistamento.Seu programa também deverá informar o tempo que falta ou
que ja passou do prazo.'''

# você pode importar 'date' da biblioteca 'datetime' para por a data atual. e digitar 'date.today().year'

nascimento = int(input('Qual seu ano de nascimento? '))

idade = 2018 - nascimento

if idade == 18:
    print('Você tem {} anos. Você tem que se apresentar esse ano.'.format(idade))
elif idade < 18:
    print('Você tem {} anos. Faltam {} anos para você se apresentar.'.format(idade,18 - idade))
else:
    print('Você tem {} anos. Seu ano de apresentação foi em {}.'.format(idade,nascimento + 18))