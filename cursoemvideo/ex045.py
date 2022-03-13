# Make a program thats make the computer to play jokenpo with you

from random import randint
from time import sleep

item = ('Rock', 'Paper', 'Scissors')
cpu = randint(0, 2)

print('\33[31mYour choices are:\33[m')
print('''[ 0 ] \33[32mRock\33[m
[ 1 ] \33[34mPaper\33[m
[ 2 ] \33[35mScissors\33[m''')
player = int(input('\33[31mWhich will you choose: \33[m'))

print('= - - - =' * 2)

print('\33[34mJO\33[m')
sleep(1)
print('\33[35mKEN\33[m')
sleep(1)
print('\33[36mPO!!!\33[m')

print('= - - - =' * 2)

if cpu == 0: # CPU chose Rock

    if player == 0:
        print('You chose Rock. CPU chose Rock:')
        print('Tied!')

    elif player == 1:
        print('You chose Paper. CPU chose Rock:')
        print('\33[32mThe Player Won!\33[m')

    elif player == 2:
        print('You chose Scissors. Cpu chose Rock:')
        print('\33[31mThe CPU Won!\33[m')

    else:
        print('\33[33mInvalid Move. Try Again!\33[m')

elif cpu == 1: # CPU chose Paper

    if player == 0:
        print('You chose Rock. CPU chose Paper:')
        print('\33[31mThe CPU Won!\33[m')

    elif player == 1:
        print('You chose Paper. CPU chose Paper')
        print('Tied!')

    elif player == 2:
        print('You chose Scissor. CPU chose Paper')
        print('\33[32mThe Player Won!\33[m')

    else:
        print('\33[33mInvalid Move. Try Again!\33[m')

elif cpu == 2: # CPU chose Scissors

    if player == 0:
        print('You chose Rock. CPU chose Scissors')
        print('\33[32mThe Player Won!\33[m')

    elif player == 1:
        print('You chose Paper. CPU chose Rock')
        print('\33[31mThe CPU Won!\33[m')


    elif player == 2:
        print('You chose Scissors. CPU chose Scissors')
        print('Tied!')

    else:
        print('\33[33mInvalid Move. Try Again!\33[m')
else:
    print('\33[33mInvalid move. Try again!\33[m')
print('= - - - =' * 2)
