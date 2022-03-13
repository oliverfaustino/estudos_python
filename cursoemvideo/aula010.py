nome = str(input('Digite seu nome: '))
if len(nome)>=10:
    print('Que nome grande!')
else:
    print('Que nome pequeno')
print('Bom dia, {}'.format(nome))