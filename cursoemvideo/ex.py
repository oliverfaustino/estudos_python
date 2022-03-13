"""print('\33[33mOlá, Mundo')
print('\33[43mOlá, Mundo\33[m')
print('\33[1;43;7mOlá, Mundo\33[m')
print('\33[3;30;45mOlá, Mundo\33[m')
print('\33[1;7mOlá, Mundo\33[m')"""

cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[37m',
         'fbranco': '\033[40m',
         'fvermelho': '\033[41m',
         'fverde': '\033[42m',
         'famarelo': '\033[43m',
         'fazul': '\033[44m',
         'froxo': '\033[45m',
         'fciano': '\033[46m',
         'fcinza': '\033[47m',
         'bold':'\033[1m',
         'underline':'\033[4m',
         'negative':'\033[7m'}
print('{}Vermelho {}Branco {}Branco{} {}Vermelho{} !!'.format(cores['vermelho'], cores ['branco'],cores ['fbranco'], cores ['limpa'], cores ['fvermelho'], cores ['limpa']))
print('\33[4;40;31mUnderline, More White Background, More Red Letter\33[m')