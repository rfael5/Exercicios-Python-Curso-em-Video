'''EXERCÍCIO 21
Faça um programa em python que abra e reproduza o audio de um arquivo MP3.'''

'''A forma que o professor mostrou na aula não deu certo porque desde que a aula foi lançada
o pygame mudou. Agora você tem que iniciar o mixer primeiro e depois iniciar o pygame. 

O professor colocou só o 'pygame.init' e já colocou a linha com o load. Mas agora você tem
que colocar o 'pygame.mixer.init()' primeiro, e depois o 'pygame.init()'.'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ai3.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''Nos comentários, mostraram o módulo playsound, que é bem mais facil que o pygame. Segue
abaixo:

import playsound
playsound.playsound('ai3.mp3')
'''