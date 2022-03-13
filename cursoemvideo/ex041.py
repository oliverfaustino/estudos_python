#The national swimming confederation needs a program that reads the year of birth of an athlete and shows his category, according to his age

#up to nine years old: child
#up to fourteen years old: infant
#up to nineteen years old: junior
#up to twenty five years old: senior
#above it: master

age = int(input('Insert the age of a athlete: '))
if age <= 9:
    print('This {} years old athlete is a child.'.format(age))
elif age <= 14:
    print('This {} years old athlete is a infant.'.format(age))
elif age <= 19:
    print('This {} years old athlete is a junior.'.format(age))
elif age <= 25:
    print ('This {} years old athlete is a senior.'.format(age))
else:
    print ('This {} years old athlete is a master.'.format(age))
