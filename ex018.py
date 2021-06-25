'''EXERCÍCIO 18
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
e tangente desse ângulo.'''

from math import sin, cos, tan, radians

ângulo = int(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ângulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ângulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ângulo, tangente))

'''Quando for mecher com seno, cosseno e tangente, você tem que converter eles pra
radianos com a função 'radians'.
    Da primeira vez deu um resultado completamente diferente do Guanabara porque eu
apenas importei as funções de seno, cosseno e tangente, porem não converti em radiano.
Mas depois que eu usei a função 'radians', deu certo.'''