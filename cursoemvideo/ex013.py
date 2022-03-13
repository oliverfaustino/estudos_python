#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual é o salário atual? R$'))
c = s + (s * 15 / 100)
print('O funcionário recebia R${:.2f}, e com o aumento de 15% ele recebe R${:.2f}'.format(s,c))