'''EXERCÍCIO 80
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    '''Se o c(c sendo o primeiro valor da lista nesse caso) for igual a 0 ou maior que qualquer 
    número na lista você o adiciona normalmente ao final da lista'''
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        '''Esse pos representa a posição que o programa está lendo. Se pos = 0, então ele está lendo
        a primeira posição na lista. Colocando "while pos < len(lista)" quer dizer que, quer dizer que
        você vai executar a ação abaixo enquanto o pos não chegar na última posição da lista.
        
        O que aquele "if" está fazendo é o seguinte: "lista[pos]" represento o valor que está na lista
        na posição do número do "pos". Por exemplo, em pos = 0, "lista[pos]" representa o número que
        está na posição 0 da lista. 
        Enquanto n for menor que o valor em lista[pos], o programa vai inserir o valor de n nesta
        posição, empurrando o número maior para a posição seguinte.
        Fazendo isso, os números menores sempre estarão na primeira posição da lista.'''
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print('=' * 30)
print(f'Você digitou os valores {lista}')




