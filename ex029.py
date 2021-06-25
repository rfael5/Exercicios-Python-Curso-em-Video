'''EXERCÍCIO 29
Escreve um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.'''

velocidade = float(input('Qual a velocidade do carro?'))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80km/h.\nDeverá pagar uma multa de R${}0.'.format(multa))
else:
    print('Tudo certo. Tenha um bom dia.')