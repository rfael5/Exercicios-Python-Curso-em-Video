'''EXERCÍCIO 34
Escreva um programa que pergunte o valor do salário de um funcionário e calcule o valor do
seu aumento.
Para os salários acima de R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''

salário = float(input('Qual é o salário do funcionário? '))

if salário > 1250:
    print('Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}.'.format(salário,salário + (salário * 0.1)))
else:
    print('Quem ganhava R${:.2f} vai passar a ganhar R${:.2f}.'.format(salário,salário + (salário * 0.15)))