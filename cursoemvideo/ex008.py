#Escreva um progama que leia um em metros e o exiba convertido em centímetros e milímetros. km hm dam m dm cm mm
m = float(input('Digite uma quantia em metros inteiros: '))
cm = m * 100
mm = m * 1000
dm = m / 10
dam = m / 10
hm = m / 100
km = m / 1000
print('A medidida {}m \nEm quilômetros é {}km \nEm hequitômetro é {}hm \nEm decâmetro é {}dam \nEm decímetros é {}dm \nEm centímetro é {:.0f}cm \nEm milímetro é {:.0f}mm'.format(m,km,hm,dam ,dm ,cm,mm))


