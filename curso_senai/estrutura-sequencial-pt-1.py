#print('''
#Faça um Programa que mostre a mensagem "Alo mundo" na tela.
#''')
#print('Alo mundo')

#print('''
#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
#''')
#num = int(input('Digite um número inteiro: '))
#print('O número digitado foi', num)

#print('''
#Faça um Programa que peça dois números e imprima a soma.
#''')
#num_1 = int(input('Escolha um número inteiro: '))
#num_2 = int(input('Escolha outro número inteiro: '))
#print('{} + {} é igual à {}'.format(num_1,num_2,num_2 + num_1))

print('''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
''')
notas = [] #lista vazia, onde será armazenado as notas
analise_confirmaçao = True #variável que servirá para dar função ao while da função CONFIG
confirmaçao = True #Variável que servirá para dar função ao while da função CONFIG
analise_numero = True #Variável para função len_notas, servirá como interruptor para o CONFIG

def desligar_sistema(): #função feita para desligar o programa
    desligar = str(input('Se deseja fechar o programa, digite: \'fechar\'. Se não, envie qualquer outra coisa. '))
    if desligar == 'fechar':
        exit()

def add_notas(notas): #função feita para poder adicionar uma nota nova, caso o usuário deseja. 
    analise = False
    while analise == False: #while para gerar um looping e ficar analisando as respostas do usuário, para assim refazer a pergunta caso ele retorne um valor indesejado. Ex: uma string.
        try:
            adiçao = float(input('Digite uma nota: '))
            type_adiçao = str(type(adiçao)) # fiz str() para poder depois analisar com o if, já que a resposta do type é <class 'nome da classe'>. Deixar apenas assim fica dando erro e eu não sei como consertar, então optei por transformar type em string, pois daí na analise com if eu poderia ignorar o erro que dava no '<'.
            if type_adiçao == '<class \'float\'>':
                analise = True
                notas.append(adiçao)
            elif type_adiçao == '<class \'int\'>':
                analise = True
                notas.append(adiçao)
        except ValueError:
            print('Valor digitado não é uma nota.')
    return notas

def calculo_media(notas): #função feita para calcular a média entre as notas. 
    nova_lista = []
    for conversor in notas:
        nova_lista.append(float(conversor))
        notas = nova_lista
        media = float(sum(notas)) / len(notas)   
    return round(media,1)
def CONFIG(analise_confirmaçao, confirmaçao): #função feita para analisar se o usuário deseja adicionar mais uma nota.
    analise_confirmaçao = False
    while (analise_confirmaçao == False):
        confirmaçao = str(input('Deseja adicionar mais uma nota? Digite \"s\" para sim ou \"n\" para não: '))
    
        if confirmaçao == 's':
            analise_confirmaçao = True
            confirmaçao = True
            nota_nova(notas, confirmaçao)
        elif confirmaçao == 'S':
            analise_confirmaçao = True
            confirmaçao = True
            nota_nova(notas, confirmaçao)

        elif confirmaçao == 'n':
            analise_confirmaçao = True
            confirmaçao = False
            len_notas(notas, analise_numero)

        elif confirmaçao == 'N':
            analise_confirmaçao = True
            confirmaçao = False
            len_notas(notas, analise_numero)

        else:
            print('Os dados não foram entregues corretamente, tente novamente.')
            analise_confirmaçao = False
    return analise_confirmaçao, confirmaçao

def len_notas(notas, analise_numero): #função feita para analisar se o tamanho da lista é o suficiente para realizer calculo de média. Ou seja, se for menor que dois, retornará um valor falso para variável, que servirá para um looping mais tarde.
    if len(notas) < 2:
        while (analise_numero == True):
            try:
                novo_num = float(input('Não dá para calcular média com apenas um número. Digite mais uma nota: '))
                float(novo_num)
                analise_numero = False
                notas.append(novo_num)
                CONFIG(analise_confirmaçao, confirmaçao)
            except ValueError:
                print("O valor não é uma nota")
    return analise_numero

def nota_nova(notas, confirmaçao):
    while confirmaçao == True: #while para gerar um looping e ficar analisando as respostas do usuário, para assim refazer a pergunta caso ele retorne um valor indesejado. Ex: uma string.
        try:
            adiçao = float(input('Digite a nova nota à ser adicionada: '))
            type_adiçao = str(type(adiçao)) # fiz str() para poder depois analisar com o if, já que a resposta do type é <class 'nome da classe'>. Deixar apenas assim fica dando erro e eu não sei como consertar, então optei por transformar type em string, pois daí na analise com if eu poderia ignorar o erro que dava no '<'.
            if type_adiçao == '<class \'float\'>':
                confirmaçao = False
                analise_confirmaçao = False
                notas.append(adiçao)
                CONFIG(analise_confirmaçao, confirmaçao)
            elif type_adiçao == '<class \'int\'>':
                confirmaçao = False
                analise_confirmaçao = False
                notas.append(adiçao)
                CONFIG(analise_confirmaçao, confirmaçao)
        except ValueError:
            print('Valor digitado não é uma nota.')
            pass
    return notas, confirmaçao

add_notas(notas)
CONFIG(analise_confirmaçao, confirmaçao)

print(''Notas: {} Média: {}''.format(notas, calculo_media(notas)))
#para analisar a resposta do usuário, se é um número ou não, se não, o comando repetirá. Isso pois, caso o tenha apenas 1 item dentro da lista, não dará para calcular média. Daí
# o programa irá pedir para que o usuário digite mais um.

print('''Faça um Programa que converta metros para centímetros.''')
while True:
    try:
        m = float(input('Digite a medida em metros para transformar em centímetros: '))   
    except ValueError:
        print('Valor inválido')
    else: 
        break

c = m * 100
print('{}m fica {}cm'.format(m,c))

print('Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.')
while True:
    try:
        r = float(input('Qual o raio do círculo? ')) #Receber o valor do raio
    except ValueError:
        print('Valor inválido')
    else:
        break

a = (r**2) * 3.14 # Calculo da área

print(f'A área do círculo é {a}')

print('Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário')
while True:
    try:
        l = float(input('Qual a medida dos lados desse quadrado? '))
    except ValueError:
        print('Valor inválido')
    else:
        break
area = l*l
print(f'A área desse quadrado é {area}m²')

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''