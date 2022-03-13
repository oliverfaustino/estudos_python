#crie um programa que leia um número Real ualquer pelo teclado e mostre na tela a sua porção (EX. Digite um número: 6.127
#O número 6.127 tem a parte interia 6.
from math import trunc
'''num = float(input('Digite um número flutante: '))
print ('a fração inteira de {} é {}'.format(num, trunc(num)))'''

num = float (input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))