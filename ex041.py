'''EXERCÍCIO 41
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

nascimento = int(input('Em qual ano o atleta nasceu? '))

idade = 2018 - nascimento #Você também pode importar 'date' da biblioteca 'datetime'

if idade <= 9:
    print('O atleta tem {} anos.\nCategoria: MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos.\nCategoria: INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos.\nCategoria: JUNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos.\nCategoria: SÊNIOR.'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos.\nCategoria: MASTER.'.format(idade))



