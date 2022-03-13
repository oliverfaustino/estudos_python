#redo the 035 challenge of the triangles by adding the ability to show what type of triangle will be formed

#equilateral: all sides are equal
#isosceles: only one side is different
#scalene: all sides are different

print('.={-•-}=.' * 5)
print('Tabela do Triângulos')
print('.={-•-}=.' * 5)
r1 = float(input('Digite um seguimento de reta: '))
r2 = float(input('Digite outro seguimento de reta: '))
r3 = float(input('Mais um seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos podem formar um triângulo ', end = '')
    if r1 == r2 and r2 == r3:
        print('equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Esses seguimentos não podem formar um triângulo')