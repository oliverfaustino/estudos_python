# Develop a program that calculates the amount to be paid for a product, considering its normal prices and payment terms

# in cash money/check: 10% discount
# in card: 5% discount
# in until 2x in the card: normal prices
# 3x or more in the card: 20% interest

prices = float(input('Price to pay: R$'))
print('\033[32m=== ° Payment Methods ° ===\033[m')
print('''[ 1 ] in cash / check
[ 2 ] on the card
[ 3 ] 2x in the card
[ 4 ] 3x or more in the card''')
choice = int(input('Your choice: '))
if choice == 1:
    print('When paying \033[33mR${}\033[m in cash or check, your purchase will have a 10% discount. Final price \033[33mR${:.2f}\033[m'.format(prices, prices - (prices * 10 / 100)))
elif choice == 2:
    print('When paying \033[34mR${}\033[m on the card, your purchase will have a 5% discount. Final price \033[34mR${:.2f}\033[m'.format(prices, prices - (prices * 5 / 100)))
elif choice == 3:
    print('When paying \033[35mR${}\033[m 2x on the card \033[35mR${:.2f}\033[m, your purchase will have the normal price'.format(prices, prices / 2))
elif choice == 4:
    choice2 = int(input('How many installments do you want? '))
    if choice2 >= 3:
        print('When paying \033[36mR${}\033[m {}x on the card, your purchase will have 20% interest. Final price \033[36mR${:.2f}\033[m, parceled out in \033[36mR${:.2f}\033[m mensal'.format(prices, choice2, prices + (prices * 20 / 100), (prices + (prices * 20 / 100)) / choice2))
    elif choice2 == 2:
        print('When paying \033[35mR${}\033[m 2x on the card \033[35mR${:.2f}\033[m, your purchase will have the normal price'.format(prices, prices / 2))
    elif choice2 == 1:
        print('When paying \033[34mR${}\033[m on the card, your purchase will have a 5% discount. Final price \033[34mR${:.2f}\033[m'.format(prices, prices - (prices * 5 / 100)))
else:
    print('Invalid option, try again')