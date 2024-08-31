#Q4
n = int(input('Enter a postive integer'))
from math import factorial


for i in range(n):
    
    for j in range(i+1):

        z = (factorial(i)//(factorial(j)*factorial(i-j)))
        print(z, end = ' ')

    print(' ')

