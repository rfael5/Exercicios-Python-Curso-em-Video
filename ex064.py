'''EXERCÍCIOS 64
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

'''MINHA SOLUÇÃO'''
n = 1
t = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        t = t + n
        cont += 1
print('Você digitou {} números e a soma deles é {}.'.format(cont, t))

'''SOLUÇÃO DO PROFESSOR
num = cont = soma = 0 #Se todas as variaves tiverem o mesmo valor vc pode fazer a atribuição assim.
num = int(input('Digite um número: '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número: '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont,soma))

Tentando explicar a lógica da versão do professor.
Ele colocou um num encima e fez o while que ia excluir o 999. Caso o primeiro número 
digitado não fosse 999, ele ia entrar dentro da condição do while. Dentro do while,
o 999 é automaticamente excluido, já que ele só funciona se o número digitado não for
999. Essa foi a forma que ele usou para excluir o 999 da contagem.'''

