p = float(input('O preço do produto é R$'))
d = 5
pd = p - (p * d/100)

print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(p, d, pd))
