d = int(input('Quantos dias alugados? '))
k = float(input('Quantos km rodados? '))
p = (d * 60) + (k * 0.15)

print('O total a pagar é R${}.'.format(p))