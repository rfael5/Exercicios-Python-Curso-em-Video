'''EXERCÍCIO 26
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra A.
- Em que posição ela aparece pela primeira vez.
- Em que posição ela aparece pela última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
#O 'rfind' manda procurar a partir do lado direito da frase.
print('A última letra A aparece na posição {}'.format(frase.rfind('A') + 1))