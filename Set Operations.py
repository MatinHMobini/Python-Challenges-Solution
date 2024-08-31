#Q8
a = []
b = []
u = []
u_extra = u
u_extrab = []
a_inter_b = []
a_union_b =[]
a_b = []
b_a = []
ab = []


for i in range(0,3):
    n = int(input('Enter a value for how many numbers you want in upcoming set'))
    for j in range(0, n):
        z = int(input('Enter a value'))
        if i == 0:
            u.append(z)
        elif i == 1:
            a.append(z)
        elif i == 2:
            b.append(z)

a1 = a
b1 = b
bcom = b
acom = a
a1_union = a1
b1_union = b1

for s in u:
    if s not in bcom:
        u_extrab.append(s)

      
for w in u_extra:
    if w in acom:
        u_extra.remove(w)



        
for k in a1:

    for m in b1:

        a1 = a
        if a1.count(k) > 1:
            a1.remove(k)
        if b1.count(m) > 1:
            b1.remove(m)
        if k == m:
            a_inter_b.append(k)
        if k not in b1:
            a_b.append(k)
        if m not in a1:
            b_a.append(m)
        
for f in a1:
    if f not in b1:
        ab.append(f)

for g in b1:
    if g not in a1:
        ab.append(g)
           
            


for p in a1:
    if p in b1:
        a1_union.remove(p)
        #notunion = True
    else:
        notunion = True
        #b_a.append(a1_union)
        
        
for t in b1:
    if t in a1:
        b1_union.remove(t)
        #notunion = True
    else:
        notunion = True
        #a_b.append(t)
fin_union = b1_union + a1_union
a_union_b.append(fin_union)




            
            
            
a_union_b.sort()
print('The A union B is = {',a_union_b, '}')
a_inter_b.sort()   
print('The A intersection B is = {',a_inter_b, '}')
print('The A - B is = {',a_b[0], '}')
print('The B - A is = {',b_a[0],',', b_a[1],'}')
u_extra.sort()
print('The A complement is = {', u_extra, '}')
u_extrab.sort()
print('The B complement is = {', u_extrab, '}')
ab.sort()
print('A ^ B is = {', ab, '}')

'''
print(u)
print(a)
print(b)
'''

    
