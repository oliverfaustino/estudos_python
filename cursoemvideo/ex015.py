#Escreva um programa que pergunte a quantidade de KM pescorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R%0,15 por Km rodado
d = int(input('Quantos Dias Você Ficou Com o Carro? '))
km = float(input('Quantos Quilômetros Você Percorreu Com o Carro? '))
r1 = d * 60
r2 = km * 0.15
r3 = r2 + r1
print ('Ficando {:.0f} dias com o caro e percorrendo {:.1f}Km com o carro, você deverá pagar R%{:.1f}'.format(d,km,r3))