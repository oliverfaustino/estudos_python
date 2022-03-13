# Faça um algoritmo que leia o preço de um produto e mostre seu noo preço com 5% de desconto.
print('preço com 5% de desconto! R$')
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto com 5% de desconto é R$',novo)
