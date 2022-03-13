#Make a progam that read two whole number and compare them, showing a mensagem on the screen:#
#--The firts number is greater#
#--The second number is greater#
#--Both numbers are equal#

num1 = int(input('Type a whole number: '))
num2 = int(input('type other whole number: '))
if num1> num2:
    print('\33[32mThe firts number is greater than the second number!')
elif num1< num2:
    print('\33[32mThe second number is greater than the firts number!')
else:
    print('\33[32mBoth numbers are the same!')