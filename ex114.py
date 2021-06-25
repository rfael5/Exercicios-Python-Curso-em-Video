'''EXERCÍCIO 114
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site do pudim não está acessível no momento.')
else:
    print('Consegui acessar o site do pudim com sucesso.')
    print(site.read())
                #^Com essa função o python mostra o código do site.