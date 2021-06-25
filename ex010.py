real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.23
euro = real / 5.68
iene = real / 0.048
rublo_russo = real / 0.071
peso_argentino = real / 0.080

print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))
print('{:.2f} euros, {:.2f} ienes, {:.2f} rublos russos, {:.2f} pesos argentinos.'.format(euro, iene, rublo_russo, peso_argentino))
