#Façaa um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule a
# mostre o comprimento da hipotenusa

'''co = float(input('Qual o comprimento do Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))'''

from math import hypot
co = float (input('Comrpimento do Cateto Oposto: '))
ca = float (input('Comprimento do Cateto Adjacente: '))
hi = hypot(co,ca)
print ('A hipotenusa vai medir {:.2f}'.format(hi))