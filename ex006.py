n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)

print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'.format(n, t))
'''Esse '.2f' é pra definir quantas casas decimais o número vai mostrar. Se tem o número 2 ali, vai mostrar
apenas duas casas decimais.'''
print('A raiz quadrada de {} vale {:.2f}.'.format(n, r))