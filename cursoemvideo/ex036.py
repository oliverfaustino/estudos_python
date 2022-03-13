#Escreva um programa para aprovar o empréstimo banca´rio para a compra de uma casa#
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar#
#Calcule o valor da prestação mensal, sabendo que ela não pode execer 30% do salário ou então o empréstimo será negado#

valorcasa = float(input('Qual o valo da casa? R$'))
salário = float(input('Qual o seu salário mensal? R$'))
anos = int(input('Em quantos anos você irá financiar essa casa? '))
prestação = valorcasa / (anos * 12)
if prestação> (salário * 30/100):
    print('\33[31mA prestação dessa casa será de {:.2f}, com o seu salário excedendo 30%, você não pode comprar essa casa, seu salário é baixo!'.format(prestação))
else:
    print('\33[35mVocê pagará R${:.2f} todos os meses por {} anos'.format(prestação, anos))