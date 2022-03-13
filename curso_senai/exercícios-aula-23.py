print('''2. Faça um programa que leia um nome de usuário e sua senha e não aceita a senha igual ao nome do usuário
mostrando uma mensagem de erro e voltado a pedir as informações.''')
usuario = str(input('Digite seu nome de usuário: '))
senha = str(input('Digite sua senha: '))
while senha == usuario:
    print('Sua senha não pode ser o mesmo que seu usuário, digite uma nova senha')
    senha = str(input('Nova senha: '))
if senha != usuario:
    print('Cadastro aprovado!')

print('---- { = . - - . = } ----')

print('''8. Faça um programa que leia 5 números e informe a soma e a média dos números''')
num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite um número inteiro: '))
num_3 = int(input('Digite um número inteiro: '))
num_4 = int(input('Digite um número inteiro: '))
num_5 = int(input('Digite um número inteiro: '))
lista = [num_1, num_2, num_3, num_4, num_5]
soma = sum(lista) 
média = soma / 5 
print('A soma dos números é: {}. E sua média é: {}.'.format(soma, média))

print('---- { = . - - . = } ----')

print('''9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50''')
for contador in range(0,51):
    if contador % 2 == 1:
        print(contador) 

print('---- { = . - - . = } ----')

print('''10. Faça um programa que receba dois números interior e gere os nú7meros interior que estão no intervalo compreendido por eles
11. Altere o programa anterior para mostrar no final da soma dos números''')
total = 0
numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input('Digite outro número inteiro: '))
for contador in range(numero_1 + 1, numero_2):
    print(contador)
    total = (total + contador)
    print('Soma: ',total)

print('---- { = . - - . = } ----')

print('''12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. 
O usuário deve infromar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo''')
tabuada = int(input('Tabuada do número: '))
for contador in range(10):
    print('{} x {} = {}'.format(tabuada, contador + 1, tabuada * (contador + 1)))