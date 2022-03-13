#Crie um algorítimo que leia um npumero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** 0.5
print('O dobro do número é {}.\n O triplo é {}\n A raiz quadrada é {:.2f}.'.format(d,t,rq))