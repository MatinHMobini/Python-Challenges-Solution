#Q2 assing
import math
n = int(input('Enter a postive integer'))
b = int(input('Enter a second postive integer'))

q = 1
r = 0

remainder = []

while q != 0:

    new = n

    q = int(n // b)

    r = n - (b* q)

    if r >= 0:

        remainder.append(r)

    n = q
    

#print(remainder)

l = len(remainder)

for i in range(1, l + 1):
    print(remainder[-i], end = ' ')




        
    


