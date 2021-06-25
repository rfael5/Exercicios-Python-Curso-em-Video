a = input('Digite algo:')

print(type(a))
print('Só tem espaço?',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabético?',a.isalpha())
print('É alfanumérico?',a.isalnum())
print('Está em maiúsculas?',a.isupper())
print('Está em minúsculas?',a.islower())
print('Está capitalizada?',a.istitle())

#FEITO COM FORMAT
print(' ')
print('FEITO COM FORMAT')

n = input('Digite algo: ')
print(('Só tem espaços? {}').format(n.isspace()))
print(('É um número? {}').format(n.isnumeric()))
print(('É alfabético? {}').format(n.isalpha()))
print(('É alfanumérico? {}').format(n.isalnum()))
print(('Está em maiúsculas? {}').format(n.isupper()))
print(('Está em minúsculas? {}').format(n.islower()))
print(('Está capitalizada? {}').format(n.istitle()))