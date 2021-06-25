'''EXERCÍCIO 85
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.'''
lista = [[],[]]
for c in range(0,7):
    a = int(input(f'Digite o {c + 1} valor: '))
    if a % 2 == 0:
        lista[0].append(a)
    else:
        lista[1].append(a)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]}')
print(f'Os valores impares são {lista[1]}')


