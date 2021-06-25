'''EXERCÍCIO 56
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
têm menos de 20 anos.'''
somaidade = 0
midade = 0
nvelho = ''
mvinte = 0
for c in range(1,5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ' ))
    somaidade+= idade
    mediaidade = somaidade / 4
    if sexo in 'Ff' and idade < 20:
        mvinte+= 1
    if c == 1 and sexo in 'Mm': #Esse 'in' faz ele aceitar tanto m maiusculo quanto minúsculo.
        midade = idade
        nvelho = nome
    if idade > midade and sexo in 'Mm':
        midade = idade
        nvelho = nome

print('A média das idades é igual a {}.'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(midade,nvelho))
print('{} das mulheres têm menos de 20 anos.'.format(mvinte))

'''TENTANDO EXPLICAR A PARTE DO HOMEM MAIS VELHO
Caso o primeiro digitado seja homem, ele sempre vai ser o mais velho, por isso o nome
que acabou de ser digitado será atribuido à variável de nome do homem mais velho, e sua
idade à idade do mais velho.

Caso em seguida aparece outro homem mais velho que o anterior, seu nome será atribuído 
à variável de nome do mais velho e sua idade à idade do mais velho.
E isso sempre irá acontecer quando aparecer um homem mais velho que o anterior.

Caso aparece uma mulher ou um homem mais novo, seu nome e sua idade não serão atribuídos
ao nome do mais velho nem à idade do mais velho, e os nomem que já foram atribuídos à essas
variáveis permanecerão inalterados.'''