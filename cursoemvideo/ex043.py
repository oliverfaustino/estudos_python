#develop a logic that reads a person's weight and height, calculates their BMI and shows their status, as shown in the table below

#Under 18.5: Underweight
#Between 18.5 and 25: ideal weight
#25 up to 30: Overweight
#30 up to 40: obesity
#above it: morbid obesity

weight = float(input('How tall are you? ( Kg ) '))
height = float(input('How much do you weigh? ( m ) '))
imc = weight / (height ** 2)
print('Your IMC is {:.1f}'.format(imc))
if imc <= 18.5:
    print('\033[32mYou are underweight!')
elif imc >= 18.5 and imc < 25:
    print('You are at the ideal weight')
elif imc >= 25 and imc < 30:
    print('You are overweight, what out')
elif imc >= 30 and imc < 40:
    print('You are obese, what out')
else:
    print('Your are at the morbid obesity! What out')
