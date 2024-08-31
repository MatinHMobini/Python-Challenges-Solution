#Q1

import math
n = int(input('Enter a postive integer'))
store = []
  
def prime_factors(num):  
      
    while num % 2 == 0:  
          
        num = num / 2
        store.append(2)
  
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
        store.append(i)
          
        while num % i == 0:  
            
            
            num = num / i
        
            
    if num > 2:
        
        
        store.append(num)  
num = n  
prime_factors(num)

        
            
#print(store)
l = len(store)
for k in store:
    z = store.count(k)
    if z > 1 :
        print(k, '^', z, end = ' * ')
        store.remove(k)

    elif z == 1 and store[-1] != k:
        print(k, ' * ', end = ' ')

    else:
        print(k, end = ' ')
    




        

            
