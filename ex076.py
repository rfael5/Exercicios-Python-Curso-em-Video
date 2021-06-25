'''EXERCÍCIO 76
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem = ('Lápis',1,
            'Borracha',2,
            'Caneta',2,
            'Caderno',15,
            'Mochila',90)
for item in range(0,len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'R${listagem[item]:>7.2f}')