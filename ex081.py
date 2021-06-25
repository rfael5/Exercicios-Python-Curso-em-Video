'''EXERCÍCIO 81
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []


while True:
    lista.append(int(input('Digite um valor: ')))
    seguir = str(input('Quer continuar? [s/n]: '))
    if seguir not in 'sn':
        print('Opção invalida')
        seguir = str(input('Quer continuar? [s/n]: '))
    if seguir in 'n':
        break
print(lista)
lista.sort(reverse=True)
print(f'Estes são os valores da lista ordenados de forma decrescente: {lista}')
print(f'Esta lista contém {len(lista)} elementos.')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')


