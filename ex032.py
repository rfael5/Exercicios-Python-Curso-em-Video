'''EXERCÍCIO 32
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import date #Módulo para o python trazer a data do dia atual.
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year #Fórmula para ler o ano atual.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    print(ano,'é bissexto.')
else:
    print(ano,'não é bissexto')