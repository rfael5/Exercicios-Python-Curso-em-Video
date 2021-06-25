'''EXERCÍCIO 57
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


s = ''
while s != 'M' and s != 'F':
    s = str(input('Informe seu sexo [M/F]: ')).strip().upper()
    if s != 'M' and s != 'F':
        print('Opção invalida')
print('Ok')

'''VERSÃO DO PROFESSOR
s = str(input('Qual seu sexo [M/F]: ')).strip().upper()
while s not in 'MmFf':
    s = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))

Essa versão do professor deu um erro. Se a pessoa digitar 'mf', o programa vai reconhecer
a primeira letra m e aceitar que o sexo m foi registrado com sucesso. No que eu fiz, esse
problema não ocorreu.'''

