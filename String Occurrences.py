#Q9
import math
list_1 = []
list_2 = []
hold = []
 
a = str(input('Enter the first string'))
b = str(input('Enter the second string'))

list_1 = list(a)
list_2 = list(b)

extra_1 = list_1
extra_2 = list_2


for i in extra_2:
   
    done1 = False
    if list_1[0] == i:
        store = extra_2.index(i)
        
        done1 = True
        
    if done1 == True and (list_1[1]) == (extra_2[store + 1]) and (list_1[2]) == (extra_2[store+2]):
        hold.append(store)
        extra_2[store] = str('*')

#print(extra_2)
rextra_2 = extra_2.reverse()
k = 0        
for j in extra_2:#[::-1]:
    
    
    rdone1 = False
    if list_1[0] == j:
        k = k + 1
        rstore = extra_2.index(j)
        
        rdone1 = True
        l = len(extra_2)
     
        
    if rdone1 == True and (list_1[1]) == (extra_2[ rstore + 1]) and (list_1[2]) == (extra_2[rstore + 2]):
        hold.append(rstore + 1 - l)
        extra_2[rstore] = str('*')

print('{', hold, '}')
#print(extra_2)






    
