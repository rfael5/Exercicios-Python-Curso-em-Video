'''EXERCÍCIO 72
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
numeros = ('zero', 'um', 'dois', 'três','quatro','cinco', 'seis', 'sete','oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0

while True:
    n = int(input('Digite um número:'))
    if n <= 20 and n >= 0:
        print(f'Você digitou o número {numeros[n]}.')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar?(Digite s ou n): ')).upper().strip()[0]
        if continuar == 'N':
            break
print('FIM')


