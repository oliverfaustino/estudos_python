#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.faça um programa que
#leia o nome dos 4 aluanos e sorteie

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será \n {}'.format(lista))