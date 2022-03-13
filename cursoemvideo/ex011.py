#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
alt = float(input('Qual é a altura da parede? '))
larg = float(input('Qual é a largura da parede? '))
m2 = alt * larg
print('A parede tem a dimensão de {} x {} e a área em metro quadrado dessa parede é {}m².'.format(alt, larg, m2))
lt = m2 / 2
print('Para pintar essa parede precisa-se de {} litros de tinta.'.format(lt))