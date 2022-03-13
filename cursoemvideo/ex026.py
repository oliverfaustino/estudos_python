'''Faça um programa que leia uma frase pelo teclado e mostre:
quantas letras A tem:
Em qual posição ela aparece primeiro:
E que posição ela aparece por último:'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('O Primeio A apareceu primeiro em {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))