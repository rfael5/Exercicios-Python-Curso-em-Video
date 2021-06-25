'''EXERCÍCIO 83
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
'''MINHA SOLUÇÃO - ESTÁ ERRADA. CONTA O NÚMERO DE PARENTESES CERTO MAS NÃO A ORDEM CERTA.
a = str(input('Digite a expressão: '))
p1 = a.count('(')
p2 = a.count(')')
print(f'{p1} parenteses abrindo e {p2} parenteses fechando.')
if p1 == p2:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')'''

'''SOLUÇÃO DO PROFESSOR'''
expressão = str(input('Digite uma expressão: '))
parenteses = []

for p in expressão:
    if p == '(':
        parenteses.append('(')
    elif p == ')':
        if len(parenteses) > 0:
            parenteses.pop() #ESSE COMANDO EXCLUI O ÚLTIMO ELEMENTO DA LISTA.
        else:
            parenteses.append(')')
            break
print(parenteses)
if len(parenteses) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')






