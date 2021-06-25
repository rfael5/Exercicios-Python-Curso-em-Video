'''EXERCÍCIO 61
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.'''

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo),end=' ')
    termo += razão
    cont+=1
print('FIM')

'''TENTANDO EXPLICAR
Você cria a variável de um contador, e faz ele valer 1.

Aí você faz um while, e manda ele somar termo com razão enquanto o contador valer 1.

Você faz o contador somar mais 1 cada vez que o termo soma com razão.

Quando o contador atingir 10, ou seja, quando o primeiro termo tiver somado com razão
10 vezes, eles vão parar de somar, formando assim uma razão com 10 termos.'''