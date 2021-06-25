'''EXERCÍCIO 48
Faça um programa que calcule a soma entre todos os números IMPARES que são MÚLTIPLOS DE
TRÊS e que se encontram no intervalo de 1 até 500.'''

'''FORMA FEITA NA AULA'''
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont,soma))

'''FORMA ALTERNATIVA COM MENOS LINHA
print(sum(range(3, 501, 6)))'''

