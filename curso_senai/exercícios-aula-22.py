''' 1. Tamanho de string. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu
comprimento. Informe também se as duas strings possuem o mesmo comprimento e são igausi ou diferentes no
 conteúdo.'''

string_1 = str(input('Digite uma palavra, ou frase: '))
string_2 = str(input('Digite uma palavra, ou frase: '))
info_string_1 = len(string_1)

print('''String 1: {}
String 2:
Tamanho de {}: {}
Tamanho de {}: {}'''.format(string_1, len(string_1), string_2, len(string_2))) 