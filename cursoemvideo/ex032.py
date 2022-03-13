#leia um ano e diz se é bissexto ou não

from datetime import date
ano = int(input('Qual ano quer analisar? Coloco 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} ano é bissexto'.format(ano))
else:
    print('{} ano não é bissexto'.format(ano))