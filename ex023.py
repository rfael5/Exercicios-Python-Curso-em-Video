'''EXERCÍCIO 23
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos 
separados por casa decimal.'''
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))

'''EXPLICAÇÃO NOS COMENTÁRIOS

Usaremos o número 1957 para fazer as contas... Este código que o Guanabara usou, poderia ser simplificado para isto
(O resultado vai ser o mesmo, pode testar):
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000

u recebe o resto da divisão inteira entre 1957 e 10 -->      1957 // 10 = 195 (10x195 = 1950),
 o resto dessa divisão é 7, logo, a unidade é 7. 
d recebe o resultado da divisão inteira entre 1957 e 10, 
esse resultado vai ser dividido por 10 novamente e pegará o resto dessa divisão, 
ficando assim:       1957 / 10 = 195(neste caso é o resultado da divisão inteira, não o resto) --> dividindo esse resultado por 10:   195 // 10 = 19 (19x10 = 190). Agora sim pegaremos o resto da divisão, que é 5. Logo, a dezena e 5.
c = Aqui é o mesmo processo anterior, 
só que dividindo por 100 -->       1957 // 100 = 19(resultado da divisão inteira). 
Agora faremos 19 // 10 = 1 (O resto dessa divisão inteira é 9). A centena é 9.
m recebe o resultado da divisão inteira entre 1957 e 1000 -->    1957 / 1000 = 1 (pronto, 1 é o milhar).

Obs: Lembre-se que divisão inteira pega apenas a parte inteira do número, 
diferente da divisão "normal" que daria valores com vírgula. '''