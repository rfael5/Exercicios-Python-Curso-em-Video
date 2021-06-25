'''EXERCÍCIO 86
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
'''MINHA SOLUÇÃO - NÃO CONSEGUI DEIXAR FORMATADO
matriz0 = [[],[],[]]
matriz1 = [[],[],[]]
matriz2 = [[],[],[]]

matriz0[0].append(int(input('Digite um valor para [0,0]: ')))
matriz0[1].append(int(input('Digite um valor para [0,1]: ')))
matriz0[2].append(int(input('Digite um valor para [0,2]: ')))
matriz1[0].append(int(input('Digite um valor para [1,0]: ')))
matriz1[1].append(int(input('Digite um valor para [1,1]: ')))
matriz1[2].append(int(input('Digite um valor para [1,2]: ')))
matriz2[0].append(int(input('Digite um valor para [2,0]: ')))
matriz2[1].append(int(input('Digite um valor para [2,1]: ')))
matriz2[2].append(int(input('Digite um valor para [2,2]: ')))
print(matriz0)
print(matriz1)
print(matriz2)'''

'''SOLUÇÃO DO PROFESSOR'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('=-' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()#Esse print faz ele saltar linha.