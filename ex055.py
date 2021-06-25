'''EXERCÍCIO 55
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o
menor peso lidos.'''

maior = 0
menor = 0

for c in range(1,6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c  == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Dos valores mostrados, {}Kg é o maior peso.'.format(maior))
print('Dos pesos mostrados, {}Kg é o menor peso.'.format(menor))

'''TENTADO EXPLICAR COMO ESSE PROGRAMA FUNCIONA
Você vai colocar no primeiro if que c = 1, esse 1 representa o primeiro valor na range. 


Logicamente, quando você digita o primeiro valor, c sempre vai ser igual ao valor 1 pois 
é o único que você digitou.

E quando c == 1, você atribui o peso que você digitou à palavra maior e à palavra menor,
como está no programa acima.
Como foi o primeiro valor que você digitou, esse valor, logicamente, vai ser tanto o maior
quanto o menor.


Feito esse primeiro if, você vai fazer o else.

Dentro do else você vai colocar outro if. Neste, caso o peso seja um valor maior do que o
valor atribuido à palavra maior acima, este novo peso será atribuído a palavra maior.
Na condição está escrito, se peso > que maior, peso será o novo maior.

Se o segundo peso for maior que o primeiro, o segundo será o novo maior, se o terceiro for 
maior que o segundo, a mesma logica é aplicada e ele será o novo maior. Cada vez que um 
maior vai aparecendo, o if faz ele substituir o maior anterior.

E a mesma coisa acontece com o menor. A cada peso menor que aparece, ele substitui o menor
anterior, e é atribuido à palavra menor.'''


