#Make a program that read the year of birth of a young person and reports, according to their age:#
#if he will still enlist in the service#
#if it's time to join the service#
#if you have passed the enlistment time#

from datetime import date

age = int(input('Enter your year of birth: '))
enlistment = (date.today().year - age)
if enlistment == 18:
    print('\33[32mYou have to enlist in the army')
elif enlistment< 18:
    print('\33[32m After {} years, you must to enlist in the army'.format(18 - enlistment))
else:
    print('\33[32mYou have passed the time of enlistment in the army!')