#pergunte a distancia de uma viagem em km.
#calcule o preço da passagem, cobrano R$0,50 por km para viagens de até 200km
#para viagens mais longas, cobre R$0,45 por km

dis = int(input('Qual a distÂncia da sua viagem em KM? '))
if dis <= 200:
    print('O valor da passagem é {}'.format(dis * 0.50))
else:
    print('O valor da passagem é {}'.format(dis * 0.45))
print('Boa viagem')