
'''Otávio Paz
5 meses atrás
Quem deu erro ao instalar o *pygame*, consegui solucionar assim:

No Pycharm:
File > Settings > Project: "Nome do seu projeto" > Project Interpreter

Clica no pip da lista e no triângulo para dar upgrade. Faça o mesmo com o setuptools.
Depois vá no "+", e digite no campo de pesquisa "pygame", clique em "install package". Espere.
Assim deve funcionar.


E o código mudou um pouco, o meu ficou assim:'''


import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass