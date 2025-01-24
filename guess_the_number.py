import random

def the_game():
    print('Welcome to the number-guessing game!\nEnter the boundaries:')
    at = input()
    while at.isdigit()==False:
        print('Enter the first number!')
        at = input()
    a = int(at)
    bt = input()        
    while bt.isdigit()==False:
        print('Enter the second number!')
        bt = input()
    b = int(bt)    
    a, b = min(a, b), max(a, b)
    number = random.randint(a, b)
    
    def is_valid(n):
        if n.isdigit():
            if b>=int(n)>=a:
                return True
            else:
                return False
        else:
            return False
            
    print(f'Enter a number from {a} to {b} (inclusive)')
    t = False
    p = 0
    while t == False:
        guess = input()
        if is_valid(guess)==False:
            print('Input invalid. Try again')
            continue
        n = int(guess)
        if n==number:
            print(f'It was {n}! Great job! It took you {p+1} tries!')
            t = True
        elif n > number:
            print('go lower')
        else:
            print('go higher')
        p+=1
    print('Would you like to play again?')
    if input().lower().startswith('y'):
        the_game()
    else:
        'Okay. Goodbye!'

the_game()        