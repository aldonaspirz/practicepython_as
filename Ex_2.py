# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

number=int(input('Podaj liczbę'))
if number==0:
    print('to jest liczba 0')
elif number%2 != 0:
    print('to jest liczba nieparzysta')
else:
    print('to jest liczba parzysta')