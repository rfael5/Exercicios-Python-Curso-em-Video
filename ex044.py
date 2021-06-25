'''EXERCÍCIO 44
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input('Preço do produto: R$'))
print('FORMA DE PAGAMENTO - DIGITE O NÚMERO CORRESPONDENTE')
print('DINHEIRO: 1\nCARTÃO À VISTA: 2\nCARTÃO 2x: 3\nCARTÃO 3x OU MAIS: 4')
pagamento = int(input('Forma de pagamento: '))

if pagamento == 1:
    print('Desconto de {:.2f}.Valor final: R${:.2f}'.format(valor * 0.1, valor - valor * 0.1))
elif pagamento == 2:
    print('Desconto de R${:.2f}. Valor final: R${:.2f}'.format(valor * 0.05,valor - valor * 0.05))
elif pagamento == 3:
    print('Valor de R${:.2f} dividido em 2x de R${:.2f}.'.format(valor,valor / 2))
elif pagamento == 4:
    parcelas = int(input('Parcelas:'))
    print('Juros de R${:.2f}.\nValor final de R${:.2f} dividido em {}x de R${:.2f}.'.format(valor * 0.2,valor *1.2,parcelas,(valor * 1.2) / parcelas))
else:
    print('FORMA DE PAGAMENTO NÃO AUTORIZADA.')