'''EXERCÍCIO 37
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão.
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número: '))
print('''CONVERTER PARA
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
conversao = int(input('Base de conversão: '))
if conversao == 1:
    print('{} em binário é igual a {}.'.format(num,bin(num)[2:]))

elif conversao == 2:
    print('{} em octal é igual a {}.'.format(num, oct(num)[2:]))

elif conversao == 3:
    print('{} em hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
                                                                #^ esse '2:' no final é pra mostrar só do 3º caracter pra frente
else:                                                           #Sem o '2:' ele mostra aqueles dois caracteres que serve pra identificar a base numérica
    print('OPÇÃO NÃO DISPONÍVEL.')