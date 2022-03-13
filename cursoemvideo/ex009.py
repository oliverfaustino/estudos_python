#faça um programa que leia um número inteiro qualquer e mostre na sua tela a tabuada
n = int(input('Digite um número para calcular a tabuada: '))
for i in range(11):
    print( n,'-x-',i,'=',n*i)