#Q3
import math
x = float(input('Enter a real number'))
n = int(input('Enter a postive integer for the number of terms in the series'))

answsinlist = []
answcoslist = []
factlist = [1]
factlist2 = [1]
fact = 1

for f in range(1,n*2):
    fact = fact * f
    factlist.append(fact)
    factlist2.append(fact)


#cos
for i in range(0, n*2 , 2):
    answcos = ((x**i)/(factlist[i]))
    answcoslist.append(answcos)
    

#sin

for j in range(1, n*2 , 2):
    
    answsin = ((x**j)/(factlist2[j]))
    answsinlist.append(answsin)

l =len(answcoslist)
for c in range(1,l,2):
    answcoslist[c] = (answcoslist[c]) * (-1)

finalcos = sum(answcoslist)
print('cos(x) is =', finalcos)

ls =len(answsinlist)
for d in range(1,ls,2):
    answsinlist[d] = (answsinlist[d]) * (-1)

finalsin = sum(answsinlist)
print('sin(x) is = ' , finalsin)

