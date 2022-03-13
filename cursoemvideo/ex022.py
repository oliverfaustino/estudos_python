'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome'''

nome = str(input('Digite Seu Nome Completo: ')).strip()
print('Seu nome todo maiúsculo é:',nome.upper())
print('Seu nome todo minúsculo é:',nome.lower())
print('Seu nome tem {} frases'.format(len(nome)- nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu priemiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))