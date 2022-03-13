#leia o comp de 3 retas e diz se pode formar um triângulo
print('.={-•-}=.' * 5)
print('Tabela de Triângulos')
print('.={-•-}=.' * 5)
r1 = float(input('Digite um seguimento de reta: '))
r2 = float(input('Digite outro seguimento de reta: '))
r3 = float(input('Mais um seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos podem formar um triângulo')
else:
    print('Esses seguimentos não podem formar um triângulo')