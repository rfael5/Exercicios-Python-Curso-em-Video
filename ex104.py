'''EXERCÍCIO 104
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

'''VERSÃO DO PROFESSOR'''
def leiaInt(msg):
    ok = False
    '''Pelo que entendi, a função desse ok é simplesmente pra ele poder dar o break depois. Mas também
    deu certo colocar o break caso a condição do if fosse atendida, e nesse caso não precisaria desse
    ok.'''
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro!Digite um número inteiro.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')


