'''EXERCÍCIO 77
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('aprender','programar','aluno','estudo','livro','computador')
a = 'palavra'
for p in palavras:
    print(f'\nNa palavra {p.upper()} as vogais são ',end=' ')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            #O lower é pra não bugar caso haja alguma palavra com letra maiuscula.
            print(vogais,end=' ')

'''Se eu entendi bem:
Quando você escreve "for p in palavra" você está escrevendo: para cada item em palavra. 
Estes itens são as palavras que estão na tupla, sendo assim, p equivale a cada uma das palavras
na tupla.
Ao escrever "for vogais em p", você está escrevendo: para cada item em p.
p são as palavras e cada item em p é uma letra da palavra.
Ao colocar o p no for, você transformou cada palavra da tupla em uma lista, e as letras nas palavras
são os itens dessa lista.'''