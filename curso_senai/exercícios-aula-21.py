''' Crie um programa que solicite a idade de um client. E logo depois, caso o cliente tenha mais de 65 anos, 
imprima a APOSENTADORIA ATIVA e caso ele tenha menos de 65 anos, imprima APOSENTADORIA RECUSADA. '''

idade = int(input('Qual a sua idade? '))

if idade >= 65:
    print('Aposentadoria Ativa')
else:
    print('Aposentadoria Recusada: Idade insuficente')

''' 2. Crie um programa que solicite 2 números, imprima na tela as seguintes informações de acordo os números
digitados.
Numero1 é maior que número2
Número2 é maior que número1
Os números são iguais '''

num_1 = int(input('Digita um número inteiro qualquer: '))
num_2 = int(input('Digita um outro número inteiro qualquer: '))
if num_1 > num_2:
    print('O {} é maior que {}!'.format(num_1,num_2))
if num_2 > num_1:
    print('O {} é maior que {}!'.format(num_2,num_1))
else:
    print('Ambos números são iguais!')

'''3. Crie um contador de 0 a 20 e imprima apenas os números maiores que 8'''
for contador in range(21):
    if contador > 8:
        print(contador)