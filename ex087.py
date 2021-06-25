'''EXERCÍCIO 87
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
'''MINHA VERSÃO'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
c3 = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        if c == 2:
            c3.append(matriz[l][c])

print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()

print(f'A soma dos valores pares é {sum(pares)}.')
print(f'A soma dos valores da terceira coluna é {sum(c3)}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')

'''VERSÃO PROFESSOR
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spares = somac3 = maiorl2 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            spares += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()

for l in range(0,3):
    somac3 += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maiorl2 = matriz[1][c]
    elif matriz[1][c] > maiorl2:
        maiorl2 = matriz[1][c]

print(f'A soma total da matriz é {spares}.')
print(f'A soma da coluna 3 é igual à {somac3}.')
print(f'O maior valor da linha 2 é {maiorl2}.')'''