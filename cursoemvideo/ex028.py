#Escreva um programa que faça o computador pensar num número inteiro de 0 a 5
#depois peça pro usuário escolher o número que o computador pensou
#após, dizer que acertou ou não

from time import sleep
from random import randint
from math import ceil
número = randint(0, 5)
print('''\33[1;32mVocê e seu computador estão em um jogo de mente. 
Tente advinhar qual número seu computador pensoum. 
Lembrando que o número vai de 0 à 5. Pronto?! Vamos começar!''')
sleep(8)
print('\33[34mEspere... ainda estou pensando\33[m')
sleep(3)
jogo = int(input('Pronto, pensei, agora tente adivinhar: '))
if jogo == número:
    print('''Seu Computador, escolheu: {}
Você escolheu: {}'''.format(número,jogo))
    print('Você conseguiu advinhar, Parabéns!')
if jogo > 5:
    print('Você é doente?! é de 0 à 5, não a mais que isso. Tente de novo!')
else:
    print('''Seu Computador, escolheu: {}
Você escolheu: {}'''.format(número,jogo))
    print('Seu computador venceu, jogue novamente!')
