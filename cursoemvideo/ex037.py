#Make a progam that reads an integer and asks the user to choice the conversion base
#- one, for binary
#- two, for octal
#- three, for hexadecyl

num = int(input('Insert a intenger: '))
print('''Choose a conversion base:
[ 1 ] conversion for binary
[ 2 ] conversion for octal
[ 3 ] conversion for hexadecyl''')
option = int(input('Your choice: '))
if option == 1:
    print ('{} for BINARY is equal to {}'.format(num, bin(num)[2:]))
elif option == 2:
    print ('{} for OCTAL is equal to {}'.format(num, oct(num)[2:]))
elif option == 3:
    print ('{} for HEXADECYL is equal to {}'.format(num, hex(num)[2:]))
else:
    print('Invalid option. Try again')