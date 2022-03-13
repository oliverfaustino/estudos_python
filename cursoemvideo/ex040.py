#make a program that reads two notes from a studant and calculates the average.
#showing a mensagem at the end, about the avarage reached

#the average is less than 5.0: fail
#the average between 5.0 and 6.0: recovery
#the average is greater than 7.0: approved

average1 = float(input('Insert students first grade: '))
average2 = float(input('Insert students second grade: '))
calculates = (average1 + average2) / 2
if calculates< 5.0:
    print('The average {} is less than 5.0: fail!'.format(calculates))
elif 7 > calculates >= 5.0:
    print('The average {} is between 5.0 and 6.9: recovery!'.format(calculates))
else:
    print('The average {} is greater than 7.0: approved!'.format(calculates))