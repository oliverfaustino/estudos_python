'''Faça um programa que calcule com FUNÇÃO o salário líquido de um funcionário'''

def calculo_salario_liquido(salario, desconto):
    liquido = salario - desconto
    return liquido
nome = str(input('Nome do empregado: '))
salario = float(input('Salário do empregago: R$'))
desconto = float(input('Desconto do empregado: R$'))

print('''Nome: {}
Salário: R${}
Desconto: R${}
Salário líquido: R${}'''.format(nome, salario, desconto, calculo_salario_liquido(salario, desconto)))

print('''
------------------------------
''')

'''Faça um programa que calcule com FUNÇÃO o valor da compra, número de parcelas e valor da parcelas'''

def calculo_parcelas(valor, num_parcelas):
    valor_parcelas = valor / num_parcelas
    return valor_parcelas
produto = str(input('Qual foi o(s) produto(s) comprado(s): '))
valor = float(input('Valor da compra: R$'))
num_parcelas = int(input('Número de parcelas: '))

print('''------------------------------
Pedido de Compra
------------------------------
Produto(s): {}
Valor: R${}
Número de Parcelas: {}
Valor das Parcelas: R${}'''.format(produto, valor, num_parcelas, calculo_parcelas(valor, num_parcelas)))