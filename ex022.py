'''EXERCÍCIO 22
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

#Usa-se o '.strip()' para excluir espaços no inicio ou final da digitação.
nome = str(input('Qual é o seu nome? ')).strip()
dividido = nome.split()

print('Analisando seu nome')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
#Usou 'len(nome) - nome.count(" ") para não contar os espaços entre o nome. Faz uma subtração, a contagem de caracteres menos a contagem de espaços.
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(" ")))
print('Seu primeiro nome tem {} letras.'.format(len(dividido[0])))
