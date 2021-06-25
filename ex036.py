'''EXERCÍCIO 36
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado.'''

vcasa = float(input('Qual o valor da casa? '))
salário = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos ele irá pagar? '))

parcelas = vcasa / (anos * 12)
strinta = salário * 0.3

if parcelas > strinta:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.\nSeu empréstimo foi negado.'.format(vcasa,anos,parcelas))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.\nEmpréstimo APROVADO.'.format(anos*12,anos,parcelas))


