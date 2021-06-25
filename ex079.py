'''EXERCÍCIO 79
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
únicos digitados, em ordem crescente. '''
lista = []

while True:
    a = int(input('Digite um valor: '))
    if a not in lista:
        lista.append(a)
    else:
        print('Esse valor já está na lista')
    p = str(input('Quer continuar?: '))
    while p != 's' and p != 'n':
        print('Comando invalido.')
        p = str(input('Quer continuar?: '))
    if p == 'n':
        break

print(sorted(lista))