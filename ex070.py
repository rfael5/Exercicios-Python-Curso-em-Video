'''EXERCÍCIO 70
Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

tcompra = menor = mmil = 0
prodmenor = ' '
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    tcompra = tcompra + preço
    if preço > 1000:
        mmil += 1
    if tcompra == preço:
        menor = preço
        prodmenor = produto
    else:
        if preço < menor:
            menor = preço
            prodmenor = produto
    if continuar == 'N':
        break
print(f'O total da compra foi R${tcompra:.2f}')
print(f'Temos {mmil} produto(s) custando mais de R$ 1000.00.')
print(f'O produto mais barado é {prodmenor} no valor de R${menor:.2f}.')

'''Para começar a fazer valer o comando do menor preço, o professor usou um contador que ia fazer
o codigo começar a valer quando o contador tivesse em 1, ou seja assim que o primeiro valor fosse
digitado.

Na versão dele ficou assim:
if cont == 1 and preço < menor:
    menor = preço
    prodmenor = produto

Ele não fez um else, com esse and ele exclui a necessidade do else.'''