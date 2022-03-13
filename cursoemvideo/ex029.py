#Escreva um programa que lei a  velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cssa Km acima do limite

km = float(input('Qual a velocidade do Carro em KM/h: '))
if km > 80.0:
    multa = (km - 80) * 7
    print('''Este carro foi multado.
    Deve pagar a multa de: R${}'''.format(multa))
print('O Km/h deste carro está adequado!')