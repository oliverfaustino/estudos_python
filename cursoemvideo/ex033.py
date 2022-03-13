#leia 3 números e amostre o maior e o menor
from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('Calculando o menor número . . .')
sleep(1)
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('Calculando o maior número . . .')
sleep(1)
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))