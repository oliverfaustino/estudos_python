from time import sleep

add = str(input(('Vamos brincar de assassinato? '))).strip().lower()
if add in 'sim' 'claro' 'aceito' 'lógico' 'com certeza' 'pode apostar' 's' 'ok' 'beleza' 'tá' 'bom' 'óbvio':
    print('\033[31mCerto! Vamos começar!')
    sleep(2)
    print('''Um assassino estaria lhe seguindo. Você acabou sendo encurralado em um beco sem saída, esse assassino tinha em mãos uma faca pontuda e afiada.
Em meio este caminho, Um golpe por parte do assassino com a faca era feito, mirando em seu estômago...''')
    sleep(5)
    resposta = str(input('O que você faria? Lembrando que suas opções são apenas, fugir, desviar, contra atacar, ficar parado. \33[m')).strip().lower()
if resposta == 'fugir':
    print('\33[m35Como vocês estavam em um beco sem saída, você acabou se encurralando e sendo pego pelo assassino, levando a sua morte!')
elif resposta == 'desviar':
    print('\33[m35Você desviou do golpe e conseguiu escapar do beco, seguindo sua corrida de vida ou morte, fazendo o assassino desistir.')
elif resposta ==  'contra atacar':
    print('\33[m35Você não estava armado, contra atacar seria burrice. Contudo, foi pego e morto!')
elif resposta == 'ficar parado':
    print('\33[m35Foi morto de forma fácil.')
else:
    print('Responda corretamente...')
print('\33[30mApós os ocorridos, a vizinhaça chamou a polícia e o assassino foi preso!')