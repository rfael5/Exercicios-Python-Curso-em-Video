'''EXERCÍCIO 31
Desenvolva um programa que pergunta a distância de uma viagem em km. Calcule o preço da
passagem, cobrando R$0,50 por km para viagens de até 200km, e R$0,45 para viagens mais longas.'''

distância = float(input('Qual é a distância da sua viagem? '))

if distância > 200:
    print('Você vai fazer uma viagem de {}km.\nE o preço da passagem será de R${}.'.format(distância, distância * 0.45))
else:
    print('Você vai fazer uma viagem de {}km.\nE o preço da passagem será de R${}'.format(distância, distância * 0.50))