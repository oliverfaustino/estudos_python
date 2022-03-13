#leia o salário
#para salários maior que R$1.250,00, calcule 10% de aumento
#para menores disso, aumenta 15$

sal = float(input('Digite o salário do funcionário: RS'))
if sal > 1250:
    print('O novo saláro é: {}'.format(sal + (sal * 10 / 100)))
else:
    print('O novo salário é: {}'.format(sal + (sal * 15 / 100)))