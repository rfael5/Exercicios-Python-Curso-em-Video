'''EXERCÍCIO 49
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''

t = int(input('Digite um número:'))

for c in range(0,11):
    print('{} x {:2} = {}'.format(t,c,c * t))
                # ^ Esse ':2' é pra deixar a tabuada toda alinhada.