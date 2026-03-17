from math import sqrt

# Function
def calculator():
     # Variable
    n1 = float(input('Enter a number: '))
    n2 = float(input('Enter another number: '))

       # Variable signal
    signal = input('Choose the calculation (answer with a number or signal):\n 1) + \n 2) - \n 3) x \n 4) ÷ \n 5) x^x \n 6) sqrt \n: ')

    # Condition
    if signal == '1' or signal == '+':
        print(f'The sum of \033[1;32m{n1}\033[m + \033[1;32m{n2}\033[m =', n1 + n2)
    elif signal == '2' or signal == '-':
        print(f'The subtraction of \033[1;32m{n1}\033[m - \033[1;32m{n2}\033[m =', n1 - n2)
    elif signal == '3' or signal == 'x':
        print(f'The multiplication of \033[1;32m{n1}\033[m x \033[1;32m{n2}\033[m = ', n1 * n2)
    elif signal == '4' or signal == '÷':
        if n2 == 0:
            print('\033[1;31mDivision by zero is not allowed.\033[m')
        else:
            print(f'The division of \033[1;32m{n1}\033[m ÷ \033[1;32m{n2}\033[m =', n1 / n2)
    elif signal == '5' or signal == 'x^x':
        print(f'The exponentiation of \033[1;32m{n1}\033[m^\033[1;32m{n2}\033[m = ', n1 ** n2)
    elif signal == '6' or signal == 'sqrt':
        n3 = sqrt(n1)
        n4 = sqrt(n2)
        print(f'The square root of \033[1;32m{n1}\033[m = \033[1;32m{n3:.3f}\033[m and \033[1;32m{n2}\033[m = \033[1;32m{n4:.3f}\033[m')

    # Repetition and Invalid answer
    again = input("Let's try again? ").lower()
    if again not in ['yes', 'y', 'sim', 'no', 'not', 'não', 'n']:
         print('\033[1;31mInvalid answer\033[m')
         exit()
    if again in ['yes', 'y', 'sim']:
        again = True
    elif again in ['no', 'not', 'não', 'n']:
        again = False
        print('\033[1;31m-=' * 20 + 'Finished' + '=-' * 20)
        exit()
    while again == True:
        calculator()

# Calling the function
calculator()