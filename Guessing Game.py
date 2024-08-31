#Q5
import random
import math

p = int(input('Enter a value for how many people are playing the game'))
guesslist = []
nameholder = []
inpt = ('Y')

while inpt == ('Y') and p != 0:

    guesscounter = 0
    guesslistholder = guesslist
    name = str(input('Enter your name'))

    nameholder.append(name)

    print(nameholder)
    
    n = int(input('Enter a non-negative integer for the range of the numbers you can guess to:'))

    x = random.randint(0,n )

    for i in range(0, n):
        
        guess = int(input('Enter a value for your guess:'))

        if x == guess:

            print('Congrats, you guessed it right!')

            p = p -1

            guesscounter = guesscounter + 1

            guesslist.append(guesscounter)

            print('You guessed it right within', guesscounter, 'attempts')
            
            if p != 0:
                inpt = str(input('Is the next player ready to begin?, if so press Y'))

            break

        elif x > guess:

            print('Your number is too low')
            guesscounter = guesscounter + 1

        elif x < guess:

            print('Your number is too high')
            guesscounter = guesscounter + 1

    
#print(guesslist)
lowest = min(guesslist)
iholder = guesslist.index(lowest)
#print(iholder)

print(nameholder[iholder],'Had the lowest attemptes to guess the right number')
print('Your number of attempts:', lowest)
    

