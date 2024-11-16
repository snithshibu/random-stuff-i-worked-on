import random

#welcoming statement
print(f"Welcome to the Random Number Guessing Game! Here you will have a chance to guess a random number. \nRules are simple, you choose your difficulty and keep guessing till you guess the right number! \nThere's no limit to how many guesses you have, so you could be here for a while.")

while True: #so that they can continue playing n number of times
    
    #they pick thier own difficulty here
    l_lim=int(input("Choose your lower range: ")) 
    u_lim=int(input("Choose your upper range: "))
    print("Happy Guessing!")

    #random number generated based on their inputted range
    number=random.randint(l_lim,u_lim) 
    guess=None
    count=1 #shows how many guesses they took at the end.
    
    while guess!=number: #keeps asking for the number until they guess the right one
        guess=int(input("Please type a number between " + str(l_lim) + " and " + str(u_lim) + ": "))
        #gives feedback to their responses
        if guess==number:
            print("You got the right number!")
        else:
            if guess > number:
                print("Go lower, try again!")
            elif guess < number:
                print("Go higher, try again!")
            else:
                pass
            count += 1
    
    #shows how many guesses they took
    if count==1: 
        print('It took you', count, 'guess!')
    else:
        print('It took you', count, 'guesses!')

    #if they want to play again
    nxt = input('Do you want to play again? Enter yes or no: ').lower()
    if nxt == 'yes':
        print('Excellent. You will play again!')
    elif nxt == 'no':
        print("Thanks for playing!")
        break
    else:
        print('Invalid input. Enter yes or no')
