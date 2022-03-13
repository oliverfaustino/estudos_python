print(' 1 - Crie um contador de 0 a 15')
for contador in range(16):
    print(contador)
print('2 - Crie um contador de 0 a 50, com incremento de 3')
for contador in range(0,50,3):
    print(contador)
print('3 - Crie um contador de 10 a 1 ( decrescente )')
for contador in range(11,0,-1):
    print(contador)
total = 0
print("4- Crie um contador de 1 a 5 e no final imprima a soma dos numeros do contador")
for contador in range(6):
    print(contador)
    total = (total + contador)
    print("Soma:",total)
começo = int(input('Digite um número inteiro para por como começo da contagem: '))
final = int(input('Digite um número inteiro para por como final da contagem: '))
for contagem in range(começo,final+1):
    print(contagem)