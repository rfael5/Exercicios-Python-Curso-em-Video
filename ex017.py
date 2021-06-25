'''EXERCÍCIO 17
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(hypot(cateto_oposto, cateto_adjacente)))

'''Abaixo estão as duas outras formas de fazer. 
Lembrando, O QUADRADO DA HIPOTENUSA, É IGUAL À SOMA DO QUADRADO DOS CATETOS.
_________________________________________________________________________________________

A primeira usando formulas matemáticas simples, sem precisar importar a biblioteca math:

somacatetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = somacatetos ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
___________________________________________________________________________________________

A segunda usando a função sqrt:

from math import sqrt

somacatetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = sqrt(somacatetos)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa)
___________________________________________________________________________________________

No exercício eu vou simplesmente usar a função da biblioteca math para fazer a hipotenusa
direto.'''

