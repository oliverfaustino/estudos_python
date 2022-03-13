#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (us$ = R# 3,27)
dc = float(input('Quanto dinheiro você tem na carteira? R$'))
d = dc / 3.27
print('Com R${:.2f} você comseguirá comprar US${:.2f} e '.format(dc,d))