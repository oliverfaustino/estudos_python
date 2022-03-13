'''Crie um programa que leia o nome de uma cidade e dica se começa ou não com 'Santo'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')